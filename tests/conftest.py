import pytest

@pytest.fixture
def card_number():
    return 7000792289606361

@pytest.fixture
def acc_number():
    return 73654108430135874305

@pytest.fixture
def num_card_or(card_number):
    return f"MasterCard {card_number}"

@pytest.fixture
def num_acc_or(acc_number):
    return f"Счет {acc_number}"

@pytest.fixture
def list_example():
    return [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]