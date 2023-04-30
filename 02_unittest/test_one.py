# to run the tests:
# > python -m unittest test_one.py
# > python -m unittest discover



import unittest
import one

class OneTest(unittest.TestCase):
    # the names must always start with "test_"
    def test_add(self):
        self.assertEqual(one.add(4, 5), 9)
        self.assertEqual(one.add(-1, 4), 3)

    def test_subtract(self):
        self.assertEqual(one.subtract(5, 0), 5)
        self.assertEqual(one.subtract(-1, -5), 4)

    def test_multiply(self):
        self.assertEqual(one.multiply(4, 5), 20)
        self.assertEqual(one.multiply(7, 0), 0)
        self.assertEqual(one.multiply(4, 'b'), 'bbbb')

    def test_division(self):
        self.assertEqual(one.division(30, 5), 6)
        self.assertRaises(ZeroDivisionError, one.division, 4, 0)

if __name__ == '__main__':
    unittest.main()


