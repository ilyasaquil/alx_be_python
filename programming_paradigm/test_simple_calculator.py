import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)           # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)          # Negative + Positive
        self.assertEqual(self.calc.add(-5, -5), -10)       # Two negatives
        self.assertEqual(self.calc.add(0, 0), 0)           # Zeros
        self.assertEqual(self.calc.add(2.5, 3.1), 5.6)     # Floats

    # --- Subtraction Tests ---
    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)      # Positive numbers
        self.assertEqual(self.calc.subtract(3, 5), -2)     # Result negative
        self.assertEqual(self.calc.subtract(-5, -5), 0)    # Equal negatives
        self.assertEqual(self.calc.subtract(0, 5), -5)     # Zero minus positive
        self.assertEqual(self.calc.subtract(5.5, 2.2), 3.3)# Floats

    # --- Multiplication Tests ---
    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(4, 3), 12)     # Positive numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)    # Negative × Positive
        self.assertEqual(self.calc.multiply(-2, -3), 6)    # Negative × Negative
        self.assertEqual(self.calc.multiply(0, 5), 0)      # Multiply by zero
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)  # Floats

    # --- Division Tests ---
    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(6, 3), 2)        # Positive numbers
        self.assertEqual(self.calc.divide(-6, 3), -2)      # Negative ÷ Positive
        self.assertEqual(self.calc.divide(-6, -3), 2)      # Negative ÷ Negative
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5)  # Floats

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-10, 0))


if __name__ == "__main__":
    unittest.main()
