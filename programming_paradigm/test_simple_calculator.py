import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(self.calc.add(-1, 1), 0)  # -1 + 1 = 0
        self.assertEqual(self.calc.add(0, 0), 0)  # 0 + 0 = 0
        self.assertEqual(self.calc.add(-5, -3), -8)  # -5 + (-3) = -8

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # 5 - 3 = 2
        self.assertEqual(self.calc.subtract(-1, 1), -2)  # -1 - 1 = -2
        self.assertEqual(self.calc.subtract(0, 0), 0)  # 0 - 0 = 0
        self.assertEqual(self.calc.subtract(-5, -3), -2)  # -5 - (-3) = -2

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)  # 3 * 4 = 12
        self.assertEqual(self.calc.multiply(-3, 4), -12)  # -3 * 4 = -12
        self.assertEqual(self.calc.multiply(0, 4), 0)  # 0 * 4 = 0
        self.assertEqual(self.calc.multiply(-3, -4), 12)  # -3 * -4 = 12

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)  # 10 / 2 = 5
        self.assertEqual(self.calc.divide(-10, 2), -5)  # -10 / 2 = -5
        self.assertEqual(self.calc.divide(0, 5), 0)  # 0 / 5 = 0
        self.assertEqual(self.calc.divide(10, 0), None)  # Division by zero

    def test_edge_cases(self):
        """Test edge cases for division and large numbers."""
        self.assertEqual(self.calc.divide(1e10, 1e5), 100000.0)  # Large number division
        self.assertEqual(self.calc.divide(-1e10, 1e5), -100000.0)  # Negative large number division
        self.assertEqual(self.calc.divide(1, 3), 0.3333333333333333)  # Decimal division


if __name__ == "__main__":
    unittest.main()
