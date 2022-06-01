import pytest


# @pytest.mark.xfail
@pytest.mark.great
def test_greater(input_value):
    assert input_value > 100


# @pytest.mark.xfail
@pytest.mark.great
def test_greater_equal(input_value):
    assert input_value >= 100


# @pytest.mark.skip
@pytest.mark.small
def test_less(input_value):
    assert input_value < 100
