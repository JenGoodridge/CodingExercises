#https://www.hackerrank.com/challenges/write-a-function
import unittest
def is_leap(year):
    return year%4 == 0 and (year % 400 == 0 or year % 100 != 0)
    
class Test(unittest.TestCase):
    def test_is_leap(self):
        self.assertEqual(is_leap(1990), False)
        self.assertEqual(is_leap(1992), True)
        self.assertEqual(is_leap(4000), True)
        self.assertEqual(is_leap(1990), False)
        self.assertEqual(is_leap(1), False)
        
unittest.main()
    
  