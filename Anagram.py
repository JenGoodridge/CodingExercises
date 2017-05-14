# This checks whether a string is an anagram of the other.
from collections import Counter


def check_for_anagram(s1, s2):
    return len(s1) == len(s2) and Counter(s1) == Counter(s2)


def checkfor_anagram(string1, string2):
    if len(string1) != len(string2):
        return False

    newstring1 = sorted(string1)
    newstring2 = sorted(string2)

    return newstring1 == newstring2

string1 = 'aaabbbc'
string2 = 'bababa'

print(checkfor_anagram(string1, string2))
