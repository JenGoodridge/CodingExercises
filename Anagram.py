# This checks whether a string is an anagram of the other.
import unittest
from collections import Counter

def check_for_anagram(s1, s2):
    return len(s1) == len(s2) and Counter(s1) == Counter(s2)

class Test(unittest.TestCase):
    def test_check_for_anagram(self):
        self.assertEqual(check_for_anagram("aba", "aab"), True)
        self.assertEqual(check_for_anagram("deed", "feed"), False)
        self.assertEqual(check_for_anagram("",""), True)
        self.assertEqual(check_for_anagram("dee","de"), False)
        
unittest.main()
    
