from typing import Iterator


def filter_by_currency(list_transactions: list[dict], currency: str = "USD") -> Iterator[dict]:
    """
    Функция возвращает итератор, который поочередно выдает транзакции,
    валюта операции поумолчанию: USD
    """

    for transaction in list_transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(list_transactions: list[dict]) -> Iterator[dict]:
    """
    Генератор, который возвращает описание каждой транзакции по очереди
    """

    for transaction in list_transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор, который возвращает номера банковских карт
    в формате XXXX XXXX XXXX XXXX
    """

    for number in range(start, end + 1):
        # Форматируем номер карты: 16 цифр, разделённых пробелами
        card_number = f"{number:016d}"
        formatted_card_number = " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_card_number
