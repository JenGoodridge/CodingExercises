# Problem parameters: code a function that takes two strings and returns
# whether the strings have less than 2 differences between each other.


def one_away(string1, string2):
    """
    >>> one_away("", "")
    True
    >>> one_away("a", "")
    True
    >>> one_away("", "a")
    True
    >>> one_away("a", "b")
    True
    >>> one_away("b", "a")
    True
    >>> one_away("ab", "bb")
    True
    >>> one_away("bb", "ab")
    True
    >>> one_away("ab", "cb")
    True
    >>> one_away("cb", "ab")
    True
    >>> one_away("ab", "ca")
    False
    >>> one_away("ca", "ab")
    False
    >>> one_away("", "aa")
    False
    >>> one_away("aa", "")
    False
    >>> one_away("aaa", "aba")
    True
    >>> one_away("aba", "aaa")
    True
    >>> one_away("aaa", "aab")
    True
    >>> one_away("aab", "aaa")
    True
    >>> one_away("cab", "bac")
    False
    >>> one_away("abc", "cbc")
    True
    >>> one_away("a", "abc")
    False
    >>> one_away("cba", "a")
    False
    """
    index = 0
    edits = 0
    length1 = len(string1)
    length2 = len(string2)
    if len(string1) > len(string2):
        maximum = len(string1)
        minimum = len(string2)
    else:
        maximum = len(string2)
        minimum = len(string1)

    # If either string is null
    if string1 == "" or string2 == "":
        if maximum - minimum > 1:
            edits = 2
        else:
            edits = 0

# If the lengths of the strings are not equal and only differ by 1
    elif len(string1) != len(string2) and -1 <= len(string1) - len(string2) <= 1 :
        edits += 1

# If the strings first chars are not the same but the last chars are the same
        if string1[0] != string2[0] and string1[length1 -1] == string2[length2 -1]:
            for index in range(minimum - 1, 0, -1):
                if string1[index] != string2[index]:
                    edits += 1
                    break

# If the first characters are the same
        else:
            for index in range(0, minimum):
                if string1[index] != string2[index]:
                    edits += 1
                    break

# If the character strings lengths are equal
    elif len(string1) == len(string2):
        for index in range(0, maximum):
            if string1[index] != string2[index]:
                edits += 1

# If the strings lengths have too many characters
    else:
        return False

    # Evaluating the return statement
    return edits <= 1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
