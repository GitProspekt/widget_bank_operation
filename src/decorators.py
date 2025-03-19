import functools

def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Формируем строку с входными параметрами
            inputs = f"Inputs: {args}, {kwargs}"

            try:
                # Логируем начало выполнения функции
                log_message = f"{func.__name__} started\n"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message, end='')

                # Выполняем функцию
                result = func(*args, **kwargs)

                # Логируем успешное завершение функции
                log_message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message, end='')

                return result
            except Exception as e:
                # Логируем ошибку, если она возникла
                log_message = f"{func.__name__} error: {type(e).__name__}. {inputs}\n"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message)
                else:
                    print(log_message, end='')
                raise  # Повторно поднимаем исключение

        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

# Тестируем функцию
my_function(1, 2)
#my_function(1, 'a')  # Это вызовет ошибку

