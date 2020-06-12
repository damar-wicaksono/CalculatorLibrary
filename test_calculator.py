"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 5 == calculator.add(3, 2)

    def test_subtraction(self):
        assert 7 == calculator.subtract(10, 3)

    def test_multiplication(self):
        assert 32 == calculator.multiply(4, 8)

    def test_division(self):
        assert 9 == calculator.divide(90, 10)
