import json
import unittest
from unittest.mock import patch

from src.Utils import sum_transaction, way_json_file


@patch(
    "builtins.open",
    new_callable=unittest.mock.mock_open,
    read_data=json.dumps([{"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}]),
)
def test_way_json_file_valid(mock_open):
    """Тест: файл успешно читается и содержит корректный JSON-список."""
    result = way_json_file("dummy_path.json")
    assert result == [{"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}]
    mock_open.assert_called_once_with("dummy_path.json", encoding="utf-8")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_way_json_file_not_found(mock_open):
    """Тест: файл не найден."""
    result = way_json_file("nonexistent_path.json")
    assert result == []
    mock_open.assert_called_once_with("nonexistent_path.json", encoding="utf-8")


@patch("builtins.open", new_callable=unittest.mock.mock_open, read_data="")
def test_way_json_file_empty(mock_open):
    """Тест: файл пустой."""
    result = way_json_file("empty_path.json")
    assert result == []
    mock_open.assert_called_once_with("empty_path.json", encoding="utf-8")


@patch("src.external_api.convert_currency", return_value=1000.0)
def test_sum_transaction_usd(mock_convert):
    """Тест: транзакция в USD конвертируется в RUB."""
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    result = sum_transaction(transaction)
    assert result == 1000.0
    mock_convert.assert_called_once_with("USD", "RUB", "100")
