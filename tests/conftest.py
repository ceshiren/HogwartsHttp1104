import pytest

from src.calc import Calc


@pytest.fixture(scope='function')
def get_calc():
    print('calc init')
    return Calc()