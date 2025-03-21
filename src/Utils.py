import json


file_way_json = 'C:\\Users\\kdo_k\\PycharmProjects\\widget_bank_operation\\data\\operations.json'

def way_json_file(file_way) -> dict:
    """Ф-я рапаковывает json файл в python"""

    with open(file_way) as f:
        data = json.load(f)
    return data

# "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
data = way_json_file(file_way_json)
def sum_transaction(transaction: dict) -> float:
    """Ф-я выдает сумму транзакции в рублях, конвертирует из USD,EUR в RUB"""
    if transaction["operationAmount"]["currency"]["code"] == "USD":
       # amount_trasaction_RUB = transaction["operationAmount"]["amount"]


    else:
        amount_trasaction_RUB = transaction["operationAmount"]["amount"]

    return amount_trasaction_RUB

# print(way_json_file(file_way_json))
# print(type(way_json_file(file_way_json)))

print(sum_transaction(data[0]))
