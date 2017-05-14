# Takes two lists of ints and checks whether the second list ints are squares
# of the first.


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

print(compareSquares(a, b))
