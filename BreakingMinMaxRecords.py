#!/bin/python3
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records
import sys
import unittest
def getRecord(s):
    minScore = s[0]
    maxScore = s[0]
    changeMax = 0
    changeMin = 0
    for game in s:
        if game > maxScore:
            changeMax += 1
            maxScore = game
        elif game < minScore:
            changeMin += 1
            minScore = game
    return (str(changeMax) + " " + str(changeMin))

    
class Test(unittest.TestCase):
    def test_getRecord(self):
        self.assertEqual(getRecord([1, 2, 3]), "2 0")
        self.assertEqual(getRecord([1]), "0 0")
        self.assertEqual(getRecord([10, 2, 5, 8, 19, 20, 1]), "2 2")
        self.assertEqual(getRecord([5, 2, 1, 0, 6, 7, 0, 8, 8, 9]), "4 3")
        
unittest.main()