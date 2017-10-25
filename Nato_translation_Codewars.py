# to_nato takes a string and returns the NATO translation of the string.
def to_nato(words):
    solution = []
    translation = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor","Whiskey", "Xray", "Yankee", "Zulu"]
    for char in words:
        if char.isalpha():
            solution.append(translation[ord(char.lower()) - 97])
        else:
            solution.append(char)

    return ' '.join(solution)

print(to_nato("The quick brown fox jumps over the lazy dog."))
print(to_nato("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.!!!"))
print(to_nato("aBc"))
print(to_nato("xyZ"))

