#https://www.hackerrank.com/challenges/sparse-arrays
# Handling file input
import fileinput
stringArray = []
queryArray = []
intArray = []
for line in fileinput.input():
    try: 
        int(line)
        intArray.append(line)
    except:
        if len(intArray) == 1: 
            stringArray.append(line.strip())
        else:
            queryArray.append(line.strip())
            
# Actual solution
queryCount = 0
for query in queryArray:
    for string in stringArray:
        if query == string:
            queryCount += 1
    print(queryCount)
    queryCount = 0