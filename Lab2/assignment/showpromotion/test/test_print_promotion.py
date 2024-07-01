import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import source.print_promotion as print_promotion

# TS001
def test_under_500():
    result = print_promotion(1)
    assert result == "Thank you and see you next time"
def test_under_500():
    result = print_promotion(250)
    assert result == "Thank you and see you next time"
def test_under_500():
    result = print_promotion(499)
    assert result == "Thank you and see you next time"
    
# TS002
def test_500_to_700():
    result = print_promotion(500)
    assert result == "Free ice cream cone = 1"
def test_500_to_700():
    result = print_promotion(600)
    assert result == "Free ice cream cone = 1"
def test_500_to_700():
    result = print_promotion(699)
    assert result =="Free ice cream cone = 1"

# TS003
def test_700_to_1200():
    result = print_promotion(700)
    assert result == "Free chocolate cake = 1"
def test_700_to_1200():
    result = print_promotion(1000)
    assert result == "Free chocolate cake = 1"
def test_700_to_1200():
    result = print_promotion(1199)
    assert result == "Free chocolate cake = 1"

# TS004
def test_equal_1200():
    result = print_promotion(1200)
    assert result == "Free ice cream cone = 1 and chocolate cake = 1"
    
# TS005
def test_morethan_1200():
    result = print_promotion(1201)
    assert result == "Free ice cream cone = 1 and chocolate cake = 1"
def test_morethan_1200():
    result = print_promotion(1700)
    assert result == "Free ice cream cone = 2 and chocolate cake = 1"
def test_morethan_1200():
    result = print_promotion(1900)
    assert result == "Free ice cream cone = 1 and chocolate cake = 2"
def test_morethan_1200():
    result = print_promotion(2400)
    assert result == "Free ice cream cone = 2 and chocolate cake = 2"