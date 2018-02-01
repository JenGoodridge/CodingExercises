# to_nato takes a string and returns the NATO translation of the string.
import unittest
def to_nato(words):
    solution = []
    translation = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor","Whiskey", "Xray", "Yankee", "Zulu"]
    for char in words:
        if char.isalpha():
            solution.append(translation[ord(char.lower()) - 97])
        else:
            solution.append(char)
    return ' '.join(solution)

class Test(unittest.TestCase):
    def test_to_nato(self):
        self.assertEqual(to_nato("The quick brown fox jumps over the lazy dog."), "Tango Hotel Echo   Quebec Uniform India Charlie Kilo   Bravo Romeo Oscar Whiskey November   Foxtrot Oscar Xray   Juliett Uniform Mike Papa Sierra   Oscar Victor Echo Romeo   Tango Hotel Echo   Lima Alfa Zulu Yankee   Delta Oscar Golf .")
        self.assertEqual(to_nato("THE QUICK BROWN FOX! JUMPS OVER THE LAZY DOG?"), "Tango Hotel Echo   Quebec Uniform India Charlie Kilo   Bravo Romeo Oscar Whiskey November   Foxtrot Oscar Xray !   Juliett Uniform Mike Papa Sierra   Oscar Victor Echo Romeo   Tango Hotel Echo   Lima Alfa Zulu Yankee   Delta Oscar Golf ?")
        self.assertEqual(to_nato("aBc"), "Alfa Bravo Charlie")
        self.assertEqual(to_nato("xyZ"), "Xray Yankee Zulu")
        
unittest.main()
