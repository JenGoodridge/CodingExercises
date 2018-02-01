#https://www.hackerrank.com/challenges/sparse-arrays
#Given a file of strings determine how many times the first batch of strings appear in the second batch
import unittest
def sparseArray(strings1, strings2):
    queries = []
    queryCount = 0
    strings1 = strings1.split()
    strings2 = strings2.split()
    for query in strings1:
        for string in strings2:
            if query == string:
                queryCount += 1
        queries.append(queryCount)
        queryCount = 0
    return queries


class Test(unittest.TestCase):
    def test_sparseArray(self):
        self.assertEqual(sparseArray("Hot the cat", "Hot chocolate, the delicious drink that warms you."), [1, 1, 0])
        self.assertEqual(sparseArray("Then there but what", "Then who what where there when there why but Then how"), [2, 2, 1, 1])
        self.assertEqual(sparseArray("aba jkl", "red blue aba non jkl jkl aba yellow"), [2, 2])
        self.assertEqual(sparseArray("", "I would walk 500 miles"), [])
unittest.main()
