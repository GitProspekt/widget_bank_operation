from datetime import datetime
from typing import Iterable

list_example = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_operation: Iterable[dict], state_function: str = "EXECUTED") -> Iterable[dict]:
    """Ф-я возвращает новый список словарей, с необх-ым знач-ем"""

    list_result_fun = []
    for every_dict_in_list in list_operation:
        for key, value in every_dict_in_list.items():
            if key == "state" and value == state_function:
                list_result_fun.append(every_dict_in_list)
    return list_result_fun


def sort_by_date(list_operation: Iterable[dict], rev: bool = True) -> Iterable[dict]:
    """Ф-я сортировки по дате"""

    return sorted(list_operation, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=rev)


# print(sort_by_date(list_example))
