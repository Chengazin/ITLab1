import pytest
from src.sum_in_base import add_in_base


@pytest.mark.parametrize("a, b, base, expected", [
    # Базовые случаи в разных системах
    ("0", "0", 2, "0"),
    ("1", "1", 2, "10"),
    ("1011", "111", 2, "10010"),
    ("7", "1", 8, "10"),
    ("9", "1", 10, "10"),
    ("99", "1", 10, "100"),
    ("FF", "1", 16, "100"),
    ("A", "B", 16, "15"),
    ("Z", "1", 36, "10"),
    # Разная длина операндов
    ("1", "11111111", 2, "100000000"),
    ("100000000", "1", 2, "100000001"),
    # Большие числа
    ("9" * 50, "1", 10, "1" + "0" * 50),
])
def test_add_in_base(a, b, base, expected):
    assert add_in_base(a, b, base) == expected


def test_invalid_base_too_small():
    with pytest.raises(ValueError):
        add_in_base("1", "1", 1)


def test_invalid_base_too_large():
    with pytest.raises(ValueError):
        add_in_base("1", "1", 37)


def test_invalid_digit_for_base():
    with pytest.raises(ValueError):
        add_in_base("2", "1", 2)