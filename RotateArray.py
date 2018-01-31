# This function takes a list of ints, and an int, n,
# and takes n elements from the end of the list,
# and moves them to the beginning of the list.
import unittest

def rotate(array, n):
    length = len(array)
    elementsToMoveOver = n % length
    return array[length - elementsToMoveOver:] + array[:length - elementsToMoveOver]

list = list(range(20))
class Test(unittest.TestCase):
    def test_rotate(self):
        self.assertEqual(rotate([1,2,3], 2), [2,3,1])
        self.assertEqual(rotate([1, 2, 3, 4, 5, 6, 7], 2), [6, 7, 1, 2, 3, 4, 5])
        self.assertEqual(rotate([1, 2, 3, 4, 5, 6, 7], 50), [7, 1, 2, 3, 4, 5, 6])

unittest.main()
    