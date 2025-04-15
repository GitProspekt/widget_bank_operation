# import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd

from src.pandas_lesson import read_csv_file_transactions


def test_read_transactions_with_empty_files():
    # Подготовка тестовых данных с пустыми полями
    test_data = """id;state;date;amount;currency_name;currency_code;from;to;description
5380041;CANCELED;2021-02-01T11:54:58Z;23789;Peso;UYU;;Счет 23294994494356835683;Открытие вклада"""

    # Создаем реальный DataFrame для теста
    test_df = pd.read_csv(StringIO(test_data), delimiter=";")
    test_df = test_df.replace({np.nan: None})

    # Создаем мок для pandas.read_csv, который будет возвращать наш тестовый DataFrame
    mock_read_csv = MagicMock(return_value=test_df)

    with patch("pandas.read_csv", new=mock_read_csv):
        # Вызываем тестируемую функцию
        result = read_csv_file_transactions("dummy_path.csv")

        # Проверяем результат
        expected_result = [
            {
                "id": 5380041,
                "state": "CANCELED",
                "date": "2021-02-01T11:54:58Z",
                "amount": 23789,
                "currency_name": "Peso",
                "currency_code": "UYU",
                "from": None,
                "to": "Счет 23294994494356835683",
                "description": "Открытие вклада",
            }
        ]

        # Проверяем, что результаты совпадают
        assert result == expected_result
        # Проверяем, что read_csv был вызван с правильными параметрами
        mock_read_csv.assert_called_once_with("dummy_path.csv", delimiter=";")


# if __name__ == '__main__':
#     unittest.main()
