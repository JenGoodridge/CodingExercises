#!/bin/python3
#https://www.hackerrank.com/challenges/camelcase/submissions/code/46232522

import sys


s = input().strip()
wordCount = 1
for char in s:
    if char.isupper():
        wordCount += 1

print(wordCount)
