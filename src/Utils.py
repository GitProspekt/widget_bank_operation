import json
import logging

from src import external_api

logger = logging.getLogger("Utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:\\Users\\kdo_k\\PycharmProjects\\widget_bank_operation\\logs\\Utils.log", mode="w", encoding="UTF-8"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


file_way_json = "C:\\Users\\kdo_k\\PycharmProjects\\widget_bank_operation\\data\\operations.json"


def way_json_file(file_way) -> list[dict]:
    """Ф-я рапаковывает json файл в python"""
    logger.debug("Распаковка json файла")
    try:
        with open(file_way, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            logger.debug("Распаковка json файла завершена")
            return data
        else:
            logger.error("Ошибка! В json файле нет списка")
            return []
    except FileNotFoundError:
        # Если файл не найден
        logger.error(f"Ошибка! json файл {file_way} не найден")
        print(f"Файл {file_way} не найден.")
        return []
    except json.JSONDecodeError:
        # Если файл пустой
        logger.error(f"Ошибка! json файл {file_way} пустой или содержит некорректный JSON")
        print(f"Файл {file_way} пустой или содержит некорректный JSON.")
        return []
    except Exception as e:
        # Обработка других исключений
        logger.error(f"Ошибка!{e}")
        print(f"Произошла ошибка: {e}")
        return []


data = way_json_file(file_way_json)
# print(data)


def sum_transaction(transaction: dict) -> float:
    """Ф-я выдает сумму транзакции в рублях, конвертирует из USD,EUR в RUB"""
    logger.debug("Конвертация валюты в RUB")
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount_transaction_RUB = transaction["operationAmount"]["amount"]
    else:
        amount_transaction_RUB = external_api.convert_currency(
            transaction["operationAmount"]["currency"]["code"], "RUB", transaction["operationAmount"]["amount"]
        )
    return float(amount_transaction_RUB)


print(sum_transaction(data[0]))
