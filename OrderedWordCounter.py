#https://www.hackerrank.com/challenges/word-order
#Takes a file and counts the number of times a string appears in the file and the order in which the strings first appear
import fileinput
from collections import Counter
from collections import OrderedDict
class OrderedCounter(Counter, OrderedDict):
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
class Main():
    
    words = []
    for line in fileinput.input():
        if not fileinput.isfirstline(): 
            words.append(line.rstrip())
    counter = OrderedCounter(words)  
    result = ""
    for key in counter:
        result = result + str(counter[key]) + " " 
    print(len(counter))
    print(result)
