#!/bin/python3
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records
import sys

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
    print(str(changeMax) + " " + str(changeMin))

    
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
