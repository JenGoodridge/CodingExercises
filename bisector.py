# Checks if there is a bisector in array such that the sum of the left side of the bisector is equal to the right.
# Bisector is defined as an element in the array that is not included in the sum
import unittest

def checkforbisector(array):
    for i in range(0, len(array)):
        if sum(array[0: i]) == sum(array[i + 1: len(array) + 1]):
            return array[i]
    return False
        

class Test(unittest.TestCase):
    def test_checkforbisector(self):
        self.assertEqual(checkforbisector([]), False)
        self.assertEqual(checkforbisector([1, 1, 7, 11, 42]), False)
        self.assertEqual(checkforbisector([1, 2, 1]), 2)
        self.assertEqual(checkforbisector([1, 2, 3, 5, 6]), 5)
        self.assertEqual(checkforbisector([1, 2, 3, 3, 2, 1]), False)
        
unittest.main()