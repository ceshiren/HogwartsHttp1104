from src.calc import Calc


class TestCalc:
    def test_sum(self):
        calc = Calc()
        assert calc.sum(1, 2, 3) == 6
        assert calc.sum(1, 1, 1) == 4
