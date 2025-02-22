from mypy.types import Union


def get_mask_card_number(num_card: Union[int]) -> str:
    """Ф-я маскировки номера карты"""

    num_card_str = str(num_card)
    if  len(num_card_str) == 16:
        num_card_two_simbol = num_card_str[4:6]
        num_card_four_one_simbol = num_card_str[0:4]
        num_card_four_two_simbol = num_card_str[-4:]
        return f"{num_card_four_one_simbol} {num_card_two_simbol}** **** {num_card_four_two_simbol}"
    else:
        return f"Error!"

def get_mask_account(num_acc: Union[int]) -> str:
    """Ф-я маскировки номера счета"""

    num_acc_str = str(num_acc)
    if len(num_acc_str) == 20:
        num_acc_four_simbol = num_acc_str[-4:]
        return f"**{num_acc_four_simbol}"
    else:
        return f"Error!"



# print(get_mask_account(73654108430135874305))
# print(get_mask_card_number(7000792289606361))
