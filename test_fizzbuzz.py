import pytest
from fizzbuzz import fizzbuzz

def test_returns_number():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"


