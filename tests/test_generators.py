import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# Тесты для ф-ии filter_by_currency


def test_filter_by_currency(list_transactions: list) -> None:
    """Ф-я - тест test_filter_by_currency"""

    result = filter_by_currency(list_transactions)
    assert next(result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(result) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


@pytest.mark.parametrize(
    "invalid_format",
    [
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                    },
                },
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        ],
        [
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                    },
                },
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            }
        ],
    ],
)
def test_filter_by_currency_invalid_format(invalid_format: list[dict]) -> None:
    """Ф-я - тест на обработку неверного формата данных"""

    with pytest.raises(KeyError):
        list(filter_by_currency(invalid_format))


def test_filter_by_currency_empty_list() -> None:
    """Ф-я - тест на пустой список транзакций"""

    empty_transactions: list = []
    # Вызов функции и преобразование генератора в список
    filtered_transactions = list(filter_by_currency(empty_transactions, "USD"))
    assert filtered_transactions == empty_transactions


# Тесты для ф-ии transaction_descriptions


def test_transaction_descriptions(list_transactions: list) -> None:
    """
    Ф-я - тест на корректные значения
    """

    result = transaction_descriptions(list_transactions)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"


@pytest.mark.parametrize(
    "invalid_format",
    [
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                    },
                },
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        ],
        [
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                    },
                },
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            }
        ],
    ],
)
def test_transaction_descriptions_invalid_format(invalid_format: list[dict]) -> None:
    """Ф-я - тест на обработку неверного формата данных"""

    with pytest.raises(KeyError):
        # Передаём список транзакций в функцию
        list(transaction_descriptions(invalid_format))


@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {
                            "name": "USD",
                            "code": "USD",
                        },
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {
                            "name": "USD",
                            "code": "USD",
                        },
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            ["Перевод организации", "Перевод со счета на счет"],
        ),
    ],
)
def test_transaction_descriptions_valid_format(transactions: list[dict], expected_descriptions: list[str]) -> None:
    """Ф-я - тест на корректный формат данных"""

    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions


def test_transaction_descriptions_empty_list() -> None:
    """Ф-я - тест на пустой список транзакций"""

    empty_transactions: list = []
    # Вызов функции и преобразование генератора в список
    filtered_transactions = list(transaction_descriptions(empty_transactions))
    assert filtered_transactions == empty_transactions


# Тесты для ф-ии card_number_generator


def test_card_number_generator() -> None:
    generator = card_number_generator(1, 5)
    expected_results = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert list(generator) == expected_results


def test_card_number_generator_empty_range() -> None:
    generator = card_number_generator(10, 5)
    assert list(generator) == []


def test_card_number_generator_large_range() -> None:
    generator = card_number_generator(9999999999999995, 9999999999999999)
    expected_results = [
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]
    assert list(generator) == expected_results


def test_card_number_generator_single_value() -> None:
    generator = card_number_generator(234, 234)
    expected_result = ["0000 0000 0000 0234"]
    assert list(generator) == expected_result


def test_card_number_generator_formatting() -> None:
    generator = card_number_generator(1234567890123456, 1234567890123456)
    expected_result = "1234 5678 9012 3456"
    result = next(generator)
    assert result == expected_result
