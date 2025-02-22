from src.masks import get_mask_card_number, get_mask_account

import pytest


def test_get_mask_card_number(card_number):
    '''Ф-я - тест правильности маск-ия номера карты'''

    assert get_mask_card_number(card_number) == "7000 79** **** 6361"
    # assert get_mask_card_number(11111111111111112) == "Error!"
    # assert get_mask_card_number(21111111111111111) == "Error!"


@pytest.mark.parametrize("invalid_formate", [
    11111111111111112,
    21111111111111111,
    13543,
    None
])
def test_get_mask_card_number_invalid(invalid_formate):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_formate)


def test_get_mask_account(acc_number):
    '''Ф-я - тест правильности маск-ия номера счета'''

    assert get_mask_account(acc_number) == "**4305"
    # assert get_mask_account(111111111111111111112) == "Error!"
    # assert get_mask_account(211111111111111111111) == "Error!"


@pytest.mark.parametrize("invalid_formate", [
    111111111111111111112,
    211111111111111111111,
    13543,
    None
])
def test_get_mask_account_invalid(invalid_formate):
    with pytest.raises(ValueError):
        get_mask_account(invalid_formate)
