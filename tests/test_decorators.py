import pytest

from src.decorators import log

# Тест для проверки успешного выполнения функции


def test_log_decorator_success(capsys) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(1, 2)
    assert result == 3

    # Перехватываем и проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "add started" in captured.out
    assert "add ok" in captured.out


# Тест для проверки обработки исключений
def test_log_decorator_error(capsys) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    with pytest.raises(TypeError):
        add(1, "a")

    captured = capsys.readouterr()
    assert "add started" in captured.out
    assert "add error: TypeError" in captured.out
