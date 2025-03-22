import logging

from mypy.types import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:\\Users\\kdo_k\\PycharmProjects\\widget_bank_operation\\logs\\masks.log",
    mode="w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(num_card: Union[int]) -> str:
    """Ф-я маскировки номера карты"""

    num_card_str = str(num_card)
    logger.debug("Проверка корректности ввода номера карты")
    if len(num_card_str) == 16:
        num_card_two_simbol = num_card_str[4:6]
        num_card_four_one_simbol = num_card_str[0:4]
        num_card_four_two_simbol = num_card_str[-4:]
        logger.info("Маскировка карты завершена")
        return f"{num_card_four_one_simbol} {num_card_two_simbol}** **** {num_card_four_two_simbol}"
    else:
        logger.error("Ошибка! ValueError: некорректный номер карты")
        raise ValueError("Некорректный номер карты")


def get_mask_account(num_acc: Union[int]) -> str:
    """Ф-я маскировки номера счета"""

    num_acc_str = str(num_acc)
    logger.debug("Проверка корректности ввода номера счета")
    if len(num_acc_str) == 20:
        num_acc_four_simbol = num_acc_str[-4:]
        logger.debug("Маскировка счета завершена")
        return f"**{num_acc_four_simbol}"
    else:
        logger.error("Ошибка! ValueError: некорректный номер счета")
        raise ValueError("Некорректный номер счета")


print(get_mask_account(73654108430135874305))
print(get_mask_card_number(70007922896063611))
