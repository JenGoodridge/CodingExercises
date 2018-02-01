# Takes a list of fractions and returns a list of those fractions converted into the least common denominator (do not reduce)
# 
#https://www.codewars.com/kata/common-denominators/train/python
import unittest
def convertFracts(list):
    if len(list) <= 1:
        return list
    else:    
        denominators = []
        for l in list:
            denominators.append(l[1])

        denom = denominators[0] * denominators[1] // euclidsDivisor(denominators[0], denominators[1])
        for d in denominators:
            if d == denominators[0]:
                continue
            else:
                denom = denom * d // euclidsDivisor(denom, d)

        for fract in list:
            div = denom // fract[1]
            fract[0] = fract[0] * div
            fract[1] = denom
        return list


def euclidsDivisor(x, y):
    if x is 0:
        return y
    elif y is 0:
        return x

    else:
        if x > y:
            return euclidsDivisor(y, x % y)
        else:
            return euclidsDivisor(x, y % x)

    
class test(unittest.TestCase):
    def test_invertFracts(self):
        self.assertEqual(convertFracts([[2,6]]), [[2,6]])
        self.assertEqual(convertFracts([[]]), [[]])
        self.assertEqual(convertFracts([[5, 15], [4, 12]]), [[20, 60], [20, 60]])
        self.assertEqual(convertFracts([[1,2], [1,3], [1, 5]]), [[15,30],[10,30], [6,30]])

unittest.main()