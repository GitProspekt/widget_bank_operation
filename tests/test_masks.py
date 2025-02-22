from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number):
    '''Ф-я - тест правильности маск-ия номера карты'''

    assert get_mask_card_number(card_number) == "7000 79** **** 6361"
    assert get_mask_card_number(11111111111111112) == "Error!"
    assert get_mask_card_number(21111111111111111) == "Error!"
    assert get_mask_card_number(13543) == "Error!"
    assert get_mask_card_number(None) == "Error!"



def test_get_mask_account(acc_number):
    '''Ф-я - тест правильности маск-ия номера счета'''

    assert get_mask_account(acc_number) == "**4305"
    assert get_mask_account(111111111111111111112) == "Error!"
    assert get_mask_account(211111111111111111111) == "Error!"
    assert get_mask_account(13543) == "Error!"
    assert get_mask_account(None) == "Error!"
