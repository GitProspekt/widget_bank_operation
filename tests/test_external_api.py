import os
import unittest
from unittest.mock import Mock, patch

from dotenv import load_dotenv

from src.external_api import convert_currency

load_dotenv()
API = os.getenv("API_KEY")


class TestConvertCurrency(unittest.TestCase):

    @patch("requests.request")
    def test_convert_currency_success(self, mock_request):
        # Настройка мок-объекта для имитации успешного ответа API
        mock_response = Mock()
        mock_response.json.return_value = {"result": 101}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        # Вызов тестируемой функции
        result = convert_currency("USD", "EUR", 100)

        # Проверка, что функция возвращает ожидаемый результат
        self.assertEqual(result, 101)
        mock_request.assert_called_once_with(
            "GET",
            "https://api.apilayer.com/exchangerates_data/convert",
            headers={"apikey": API},
            params={"from": "USD", "to": "EUR", "amount": 100},
        )

    @patch("requests.request")
    def test_convert_currency_failure(self, mock_request):
        # Настройка мок-объекта для имитации неудачного ответа API
        mock_response = Mock()
        mock_response.json.return_value = {"error": "Invalid currency"}
        mock_response.status_code = 400
        mock_request.return_value = mock_response

        # Проверка, что функция выбрасывает исключение при ошибке API
        with self.assertRaises(KeyError):
            convert_currency("USD", "FFF", 100)
