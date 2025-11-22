
import unittest

# Basic math operations to be tested.
def add(x, y):
    """ Return the sum of x and y. """
    return x + y

def subtract(x, y):
    """ Return the difference of x and y. """
    return x - y

def multiply(x, y):
    """ Return the product of x and y. """
    return x * y

def divide(x, y):
    """ Return the quotient of x and y. Raise ValueError on division by zero. """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

class TestMathOperations(unittest.TestCase):
    """ Unit tests for math operations. """
    def test_add(self):
        """ Test addition. """
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        """ Test subtraction. """
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        """ Test multiplication. """
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-3, -4.5), 13.5)

    def test_divide(self):
        """ Test division. """
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(9, -2), -4.5)
        with self.assertRaises(ValueError):
            divide(2, 0)

if __name__ == '__main__':
    unittest.main()