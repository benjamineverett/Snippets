import pytest


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('x must be a string.')
    return x.capitalize()


def test_capital_case1():
    # input is lower
    assert capital_case('all lower') == 'All lower'


def test_capital_case2():
    # input is already capitalized.
    assert capital_case('All lower') == 'All lower'


def test_capital_case3():
    # Check for passing something other than a string.
    with pytest.raises(TypeError):
        capital_case(1)
