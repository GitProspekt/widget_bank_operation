import pytest

from src.widget import get_dat, mask_account_card

# Тесты для ф-ии mask_account_card


def test_mask_account_card(num_card_or: str) -> None:
    """Ф-я - тест, которая корректно распознает и применяет нужный тип маскировки"""

    assert mask_account_card(num_card_or) == "MasterCard 7000 79** **** 6361"


def test_mask_account_acc(num_acc_or: str) -> None:
    """Ф-я - тест, которая корректно распознает и применяет нужный тип маскировки"""

    assert mask_account_card(num_acc_or) == "Счет **4305"


@pytest.mark.parametrize(
    "invalid_formate",
    [
        "Счет 736541084301358743050101010101",
        "Счет 7365410843013587 4305",
        "MasterCard 70007922896063610101010101",
        "MasterCard 7000 7922 8960 6361" "13543",
    ],
)
def test_mask_account_card_invalid(invalid_formate: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(invalid_formate)


@pytest.mark.parametrize(
    "num_card_or, expected",
    [
        ("MasterCard 7000792289606361", "MasterCard 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_acc(num_card_or: str, expected: str) -> None:
    assert mask_account_card(num_card_or) == expected


# Тесты для ф-ии get_dat


@pytest.mark.parametrize(
    "data_not_format, expected",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ],
)
def test_get_dat(data_not_format: str, expected: str) -> None:
    assert get_dat(data_not_format) == expected


def test_get_dat_invalid_format() -> None:
    with pytest.raises(ValueError):
        get_dat("2019-07-03T2025")
