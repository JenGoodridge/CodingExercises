# This function takes a list of ints, and an int, n,
# and takes n elements from the end of the list,
# and moves them to the beginning of the list.


def rotate(array, n):
    length = len(array)
    elementsToMoveOver = n % length
    return array[length - elementsToMoveOver:] + array[:length - elementsToMoveOver]

list = list(range(200))
print(list)
print(rotate(list, 9))
