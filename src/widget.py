from datetime import datetime

import masks


def mask_account_card(num_card_or_acc: str) -> str:
    """Ф-я маскировки номера карты или счета"""

    if "Счет" in num_card_or_acc:
        num_acc = num_card_or_acc[-20:]
        num_acc_masks = masks.get_mask_account(int(num_acc))
        masks_fun = num_card_or_acc[:-20] + num_acc_masks
    else:
        num_card = num_card_or_acc[-16:]
        num_card_masks = masks.get_mask_card_number(int(num_card))
        masks_fun = num_card_or_acc[:-16] + num_card_masks
    return masks_fun


def get_dat(date_unformate: str) -> str:
    """Ф-я преобразование строки в заданный формат даты"""

    formatted_date = datetime.strptime(date_unformate, "%Y-%m-%dT%H:%M:%S.%f")
    return formatted_date.strftime("%d.%m.%Y")


# print(mask_account_card("MasterCard 7158300734726758"))
# print(get_dat("2019-07-03T18:35:29.512364"))
# print(get_dat("2018-06-30T02:08:58.425572"))
# print(get_dat("2018-09-12T21:27:25.241689"))
# print(get_dat("2018-10-14T08:21:33.419441"))
