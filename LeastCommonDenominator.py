# Takes a list of fractions and returns a list of those fractions converted
# into the least common denominator.


def invertFracts(list):
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


print(invertFracts([[1, 2], [1, 10], [1, 20], [1, 30], [10, 100]]))
