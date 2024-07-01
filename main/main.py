"""Module description"""
import pytest
from .fun_to_test import *


class Klass:
    """
    asdasdasd
    """
    def __init__(self, par1: str):
        """
        asdasdsad
        :param par1:
        """
        self.par1 = par1

    def return_par1_upper(self):
        """
        asdasdasdasd
        :return:
        """
        return self.par1.upper()

    def return_par2_lower(self):
        """
        asdasdasdsad
        :return:
        """
        return self.par1.lower()


class K1:
    """
    asdasdgfdgdf
    """
    def __init__(self):
        """
        asdgfhgfd
        """
        self.parameter = "this is class K1"

    def return_param_upper(self):
        """
        fdfsfsdfsdf
        :return:
        """
        return self.parameter.upper()

    def return_parameter(self):
        """
        gfdfgdfgdrf
        :return:
        """
        return self.parameter


def test_simple_fixture(simple_fixture):
    """
    dsffsdfsdf
    :param simple_fixture:
    :return:
    """
    for _ in range(100):
        assert simple_fixture != 2


@pytest.mark.parametrize(
    'param1',
    ['abC', 'CAb',]
)
def test_extended_fixture_upper(upper_fixture):
    """
    sdfsdfdsfsdf
    :param upper_fixture:
    :return:
    """
    a = upper_fixture
    assert a.isupper()


@pytest.mark.parametrize(
    'param1',
    ['abC', 'CAb',]
)
def test_extended_fixture_lower(lower_fixture):
    """
    sdfsdfsdfsdfds
    :param lower_fixture:
    :return:
    """
    a = lower_fixture
    assert a.lower()


def test_simple_power():
    """
    test_simple_power
    :return:
    """
    num = 2
    assert pow(num, 2) == simple_power(num)


def test_simple_class_return(simple_class_return):
    """
    sdfhgfghfghfgh
    :param simple_class_return:
    :return:
    """
    ret_from_class = simple_class_return
    assert ret_from_class == "this is class K1"


def test_simple_upper():
    """
    test_simple_upper
    :return:
    """
    text = 'asdasdasd'
    assert text.upper() == simple_upper(text)


@pytest.mark.parametrize('parameter', ['asdas', 1, 'uyiyuiyu'])
def test_parametrize(parameter):
    """
    sdfhggfheruyyuy
    :param parameter:
    :return:
    """
    assert isinstance(parameter, str)


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


def test_simple_add():
    """
    simple_add
    :return:
    """
    num1, num2 = 5, 6
    assert num1+num2 == simple_add(num1, num2)
