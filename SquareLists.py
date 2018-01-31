# Takes two lists of ints and checks whether the second list ints are squares
# of the first.
import unittest

def compareSquares(aa, bb):
    aa = sorted(aa)
    bb = sorted(bb)
    if len(aa) is not len(bb):
        return False
    for int in range(0, len(aa)):
        if aa[int] * aa[int] != bb[int]:
            return False
    return True

a = [2, 4, 12]
b = [4, 16, 144]

class test(unittest.TestCase):
    def test_compareSquares(self):
        self.assertEqual(compareSquares([2,4,12], [4, 16, 144]), True)
        self.assertEqual(compareSquares([9,2,100], [9, 2, 100]), False)
        self.assertEqual(compareSquares([3, 5, 6, 10], [25, 9, 100, 36]), True)
        self.assertEqual(compareSquares([], [4]), False)
        self.assertEqual(compareSquares([32], [1024]), True)
        
unittest.main()