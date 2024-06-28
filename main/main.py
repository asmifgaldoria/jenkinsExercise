from .fun_to_test import *
import pytest


def test_simple_power():
    num = 2
    assert pow(num, 2) == simple_power(num)


def test_simple_upper():
    text = 'asdasdasd'
    assert text.upper() == simple_upper(text)


def test_simple_return():
    text = 'asdasdas'
    assert text == simple_return(text)
