# Given a number n, create a method that creates a staircase with n levels.
import unittest
def staircase(n):
    for lineNumber in range(1, n + 1):
        print((n - lineNumber) * " " + lineNumber * "#")


class Test(unittest.TestCase):
    def test_staircase(self):
        self.assertEqual(staircase(2), None)
        self.assertEqual(staircase(7), None)
        
unittest.main()
