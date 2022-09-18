from django.test import TestCase
from . import Calculator

class CalculatorTestCase(TestCase):
    def setUp(self):
        # self.assertIn(5,Calculator.Calculator.Calc(num1=2,num2=3))
        Calculator.Calculator.Calc(num1=2,num2=3)
        Calculator.Calculator.Calc(num1=3,num2=4)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        test1 = Calculator.Calculator.Calc(num1=2,num2=3)
        test2 = Calculator.Calculator.Calc(num1=2,num2=3)
        self.assertEqual(test1, 5)
        self.assertEqual(test2, 5)

# Create your tests here.
