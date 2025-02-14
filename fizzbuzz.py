import pytest
from fizzbuzz import fizzbuzz

def test_returns_fizz():
    assert fizzbuzz(3) == "Fizz"  # Очакваме Fizz за число, делимо на 3
