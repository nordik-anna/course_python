import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

def test_multiply_calculate_correctly(self):
    assert self.calc.multiply(self, 9, 5) == 45

def test_division_calculate_correctly(self):
    assert self.calc.division(self, 150, 3) == 50

def test_substraction_calculate_correctly(self):
    assert self.calc.substraction(self, 120, 25) == 95

def test_adding_calculate_correctly(self):
    assert self.calc.adding(self, 99, 1) == 100
