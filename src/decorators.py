import functools
from typing import Any, Optional

"""Декоратор, который автоматически логирует начало и конец выполнения ф-и,
   а также рез-ты или ошибки"""


def log(filename: Optional[str] = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Формируем строку с входными параметрами
            inputs = f"Inputs: {args}, {kwargs}"

            try:
                # Логируем начало выполнения функции
                log_message = f"{func.__name__} started\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")

                # Выполняем функцию
                result = func(*args, **kwargs)

                # Логируем успешное завершение функции
                log_message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")

                return result
            except Exception as e:
                # Логируем ошибку, если она возникла
                log_message = f"{func.__name__} error: {type(e).__name__}. {inputs}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")
                raise  # Повторно поднимаем исключение

        return wrapper

    return decorator


"""Применяем декоратор"""


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y
