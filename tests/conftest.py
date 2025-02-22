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