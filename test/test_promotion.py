import pytest
from source.print_promotion import print_promotion

# TS001
@pytest.mark.parametrize("total_cost", [1, 250, 499])
def test_under_500(total_cost):
    result = print_promotion(total_cost)
    assert result == "Thank you and see you next time"

# TS002
@pytest.mark.parametrize("total_cost", [500, 600, 699])
def test_500_to_700(total_cost):
    result = print_promotion(total_cost)
    assert result == "Free ice cream cone = 1"

# TS003
@pytest.mark.parametrize("total_cost", [700, 1000, 1199])
def test_700_to_1200(total_cost):
    result = print_promotion(total_cost)
    assert result == "Free chocolate cake = 1"

# TS004
def test_equal_1200():
    total_cost = 1200
    result = print_promotion(total_cost)
    assert result == "Free ice cream cone = 1 and Free chocolate cake = 1"

# TS005
@pytest.mark.parametrize("total_cost, expected_output", [
    (1201, "Free ice cream cone = 1 and Free chocolate cake = 1"),
    (1700, "Free ice cream cone = 2 and Free chocolate cake = 1"),
    (1900, "Free ice cream cone = 1 and Free chocolate cake = 2"),
    (2400, "Free ice cream cone = 2 and Free chocolate cake = 2")
])
def test_morethan_1200(total_cost, expected_output):
    result = print_promotion(total_cost)
    assert result == "Free ice cream cone = 1 and Free chocolate cake = 1"
