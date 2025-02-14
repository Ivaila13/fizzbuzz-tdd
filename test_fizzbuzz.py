import pytest
from fizzbuzz import fizzbuzz

def test_returns_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"


