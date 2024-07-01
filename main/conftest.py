""" fsdfsdfsdf """
import random
import pytest
from .main import K1, Klass


@pytest.fixture(name="simple_fixture")
def return_random_int():
    """
    gdfghghfdgdf
    :return:
    """
    return random.randint(0, 1)


@pytest.fixture(name="simple_class_return")
def return_from_class():
    """
    dfgdfgfdgdfg
    :return:
    """
    k1 = K1()
    return k1.return_parameter()


@pytest.fixture(name="upper_fixture")
def upper_fixture(param1):
    """
    gfdgdfgfdg
    :param param1:
    :return:
    """
    kl = Klass(param1)
    return kl.return_par1_upper()


@pytest.fixture(name="lower_fixture")
def lower_fixture(param1):
    """
    sdfdsfsdfsdf
    :param param1:
    :return:
    """
    kl = Klass(param1)
    return kl.return_par2_lower()
