import unittest

from example import add, div, BadDenominatorError

class TestDiv(unittest.TestCase):
    def testDivisible(self):
        self.assertEqual(div(10, 5), 2)
    def testNotDivisible(self):
        self.assertEqual(div(10, 4), 2.5)
    def testNotDivisible2(self):
        self.assertAlmostEqual(div(10, 7), 1.42857, 5)
    def testDivByZero(self):
        with self.assertRaises(BadDenominatorError):
            div(10, 0)


def test_add_zero():
    assert add(5, 0) == 5

def test_add_nonzero():
    assert add(5, 2) == 7
