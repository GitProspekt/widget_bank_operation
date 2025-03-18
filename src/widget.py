from datetime import datetime

from src import masks


def mask_account_card(num_card_or_acc: str) -> str:
    """Ф-я маскировки номера карты или счета"""

    search_num = num_card_or_acc.split()
    num = search_num[-1]
    if num.isdigit() and len(num) == 20:
        num_acc_masks = masks.get_mask_account(int(num))
        masks_fun = num_card_or_acc[:-20] + num_acc_masks
    elif num.isdigit() and len(num) == 16:
        num_card_masks = masks.get_mask_card_number(int(num))
        masks_fun = num_card_or_acc[:-16] + num_card_masks
    else:
        raise ValueError("Некорректный номер карты или счета")

    return masks_fun


def get_dat(date_unformate: str) -> str:
    """Ф-я преобразование строки в заданный формат даты"""

    try:
        formatted_date = datetime.strptime(date_unformate, "%Y-%m-%dT%H:%M:%S.%f")
        return formatted_date.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректный формат даты")


# print(mask_account_card("MasterCard 7158300734726758"))
# Счет 64686473678894779589

# print(get_dat(""))
# print(get_dat("2018-06-30T02:08:58.425572"))
# print(get_dat("2018-09-12T21:27:25.241689"))
# print(get_dat("2018-10-14T08:21:33.419441"))
