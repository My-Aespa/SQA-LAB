# test_mycalculator_functions.py

import pytest
import sys
import os

# Adjust the path to your module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../source')))

import mycalculator_functions

def test_add_two_numbers():
    result = mycalculator_functions.add_two_number(number_one=3, number_two=5)
    assert result == 8

def test_subtract_two_numbers():
    result = mycalculator_functions.subtract_two_number(number_one=3, number_two=5)
    assert result == -2  # Adjusted expected result assuming subtraction function

def test_multiply_two_numbers():
    result = mycalculator_functions.multiply_two_number(number_one=3, number_two=5)
    assert result == 15

def test_divide_two_numbers():
    result = mycalculator_functions.divide_two_number(number_one=10, number_two=5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = mycalculator_functions.divide_two_number(number_one=5, number_two=0)
