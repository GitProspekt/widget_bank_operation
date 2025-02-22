from datetime import datetime

# from typing import Iterable


list_example = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_operation: list[dict], state_function: str = "EXECUTED") -> list[dict]:
    """Ф-я возвращает новый список словарей, с необх-ым знач-ем"""

    list_result_fun = []
    for every_dict_in_list in list_operation:
        if every_dict_in_list.get("state") == state_function:
            list_result_fun.append(every_dict_in_list)
    return list_result_fun


def sort_by_date(list_operation: list[dict], rev: bool = True) -> list[dict]:
    """Ф-я сортировки по дате"""

    new_list_operation = []
    try:
        for every_dict_in_list in list_operation:
            if every_dict_in_list.get("date") == None:
                continue
            elif every_dict_in_list.get("date"):
                new_list_operation.append(every_dict_in_list)
        return sorted(new_list_operation, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=rev)
    except ValueError:
        raise ValueError("Некорректный формат даты")


# print(filter_by_state(list_example))
print(sort_by_date(list_example))
