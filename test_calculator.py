"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 5 == calculator.add(3, 2)

    def test_subtraction(self):
        assert 7 == calculator.subtract(10, 3)
