import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
from print_promotion import print_promotion

def test_under_500():
    result = print_promotion(1)
    assert result == "Thank you and see you next time"
def test_500_to_700():
    result = print_promotion(500)
    assert result == 8
def test_700_to_1200():
    result = print_promotion(700)
    assert result == 8
def test_equal_1200():
    result = print_promotion(1200)
    assert result == 8
def test_morethan_1200():
    result = print_promotion(1900)
    assert result == 8