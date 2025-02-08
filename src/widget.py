import Masks


def mask_account_card(num_card_or_acc: str) -> str:
    """Ф-я маскировки номера карты или счета"""

    if "Счет" in num_card_or_acc:
        num_acc = num_card_or_acc[-20:]
        num_acc_masks = Masks.get_mask_account(int(num_acc))
        masks = num_card_or_acc[:-20] + num_acc_masks
    else:
        num_card = num_card_or_acc[-16:]
        num_card_masks = Masks.get_mask_card_number(int(num_card))
        masks = num_card_or_acc[:-16] + num_card_masks
    return masks


def get_dat(date_unformate: str) -> str:
    """Ф-я преобразование строки в заданный формат даты"""

    day = date_unformate[8:10]
    month = date_unformate[5:7]
    year = date_unformate[0:4]
    return f'{day}.{month}.{year}'


#print(mask_account_card("MasterCard 7158300734726758"))
#print(get_dat("2024-03-11T02:26:18.671407"))