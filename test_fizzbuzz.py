import pytest
from fizzbuzz import fizzbuzz

def test_returns_number():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"


