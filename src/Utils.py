import json

from src import external_api

file_way_json = "C:\\Users\\kdo_k\\PycharmProjects\\widget_bank_operation\\data\\operations.json"


def way_json_file(file_way) -> list[dict]:
    """Ф-я рапаковывает json файл в python"""
    try:
        with open(file_way, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except FileNotFoundError:
        # Если файл не найден
        print(f"Файл {file_way} не найден.")
        return []
    except json.JSONDecodeError:
        # Если файл пустой
        print(f"Файл {file_way} пустой или содержит некорректный JSON.")
        return []
    except Exception as e:
        # Обработка других исключений
        print(f"Произошла ошибка: {e}")
        return []


data = way_json_file(file_way_json)
# print(data)


def sum_transaction(transaction: dict) -> float:
    """Ф-я выдает сумму транзакции в рублях, конвертирует из USD,EUR в RUB"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount_trasaction_RUB = transaction["operationAmount"]["amount"]
    else:
        amount_trasaction_RUB = external_api.convert_currency(
            transaction["operationAmount"]["currency"]["code"], "RUB", transaction["operationAmount"]["amount"]
        )
    return float(amount_trasaction_RUB)


# print(sum_transaction(data[2]))
