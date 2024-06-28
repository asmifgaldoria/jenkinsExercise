"""Module description"""
from .fun_to_test import *


def test_simple_power():
    """
    test_simple_power
    :return:
    """
    num = 2
    assert pow(num, 2) == simple_power(num)


def test_simple_upper():
    """
    test_simple_upper
    :return:
    """
    text = 'asdasdasd'
    assert text.upper() == simple_upper(text)


def test_simple_return():
    """
    test_simple_return
    :return:
    """
    text = 'asdasdas'
    assert text == simple_return(text)


def test_simple_multi():
    """
    test_simple_multi
    :return:
    """
    num = 5
    assert 5*2 == simple_multi(num)
