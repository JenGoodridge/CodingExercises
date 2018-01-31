#!/bin/python3
#https://www.hackerrank.com/challenges/camelcase/submissions/code/46232522
import unittest
import sys
def camelCaseCounter(s):
    caseCount = 0
    for char in s:
        if char.isupper():
            caseCount += 1
    return caseCount
    
class Test(unittest.TestCase):
    def test_camelCaseCounter(self):
        self.assertEqual(camelCaseCounter("HEre"), 2)
        self.assertEqual(camelCaseCounter(""), 0)
        self.assertEqual(camelCaseCounter("HEreIamRock MELikeAHuRRiCanE212."), 13)
        self.assertEqual(camelCaseCounter("toBeOR noT To BEE"), 8)
        
unittest.main()
    

