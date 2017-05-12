# Checks if there is a bisector in array that checks whether the sum
# of the left side of the bisector is equal to the right side of the bisector


def checkforbisector(array):
    for index in array:
        x = len(array)
        a = array[0: index]
        b = array[index + 1: x]
        if sum(a) == sum(b):
            print("a is: " + str(a) + " b is " + str(b))
            print("Yes")
            break
        else:
            continue

array = [1, 9, 1]
checkforbisector(array)
