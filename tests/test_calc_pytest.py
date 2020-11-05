import pytest

from src.calc import Calc


def test_sum():
    assert 9 == 9


def test_sum2(get_calc):
    assert get_calc.sum(5, 6, 7) == 18


class TestCalcPytest:

    def setup_class(self):
        print("setup class only run once")
        self.calc = Calc()

    def setup(self):
        print("setup run before every testcase")

    @pytest.mark.it
    @pytest.mark.parametrize('first, second, expect', [
        [2, 1, 2],
        [3, 1, 3],
        [0, 3, 0],
        [0.3, 0.1, 3]
    ])
    def test_div(self, first, second, expect):
        assert self.calc.div(first, second) == expect

    @pytest.mark.e2e
    def test_mul(self):
        assert self.calc.mul(1, 2) == 2

    def teardown(self):
        print('teardown')

    def teardown_class(self):
        print('teardown class')
