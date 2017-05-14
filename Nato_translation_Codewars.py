# to_nato takes a string and returns the NATO translation of the string.
def to_nato(words):
    inp = list(words)
    solution = []
    for char in inp:
        if char == ' ':
            continue

        elif char == 'a' or char == 'A':
            solution.append('Alfa')

        elif char == 'b' or char == 'B':
            solution.append('Bravo')

        elif char == 'c' or char == 'C':
            solution.append('Charlie')

        elif char == 'd' or char == 'D':
            solution.append('Delta')

        elif char == 'e' or char == 'E':
            solution.append('Echo')

        elif char == 'f' or char == 'F':
            solution.append('Foxtrot')

        elif char == 'g' or char == 'G':
            solution.append('Golf')

        elif char == 'h' or char == 'H':
            solution.append('Hotel')

        elif char == 'i' or char == 'I':
            solution.append('India')

        elif char == 'j' or char == 'J':
            solution.append('Juliett')

        elif char == 'k' or char == 'K':
            solution.append('Kilo')

        elif char == 'l' or char == 'L':
            solution.append('Lima')

        elif char == 'm' or char == 'M':
            solution.append('Mike')

        elif char == 'n' or char == 'N':
            solution.append('November')

        elif char == 'o' or char == 'O':
            solution.append('Oscar')

        elif char == 'p' or char == 'P':
            solution.append('Papa')

        elif char == 'q' or char == 'Q':
            solution.append('Quebec')

        elif char == 'r' or char == 'R':
            solution.append('Romeo')

        elif char == 's' or char == 'S':
            solution.append('Sierra')

        elif char == 't' or char == 'T':
            solution.append('Tango')

        elif char == 'u' or char == 'U':
            solution.append('Uniform')

        elif char == 'v' or char == 'V':
            solution.append('Victor')

        elif char == 'w' or char == 'W':
            solution.append('Whiskey')

        elif char == 'x' or char == 'X':
            solution.append('Xray')

        elif char == 'y' or char == 'Y':
            solution.append('Yankee')

        elif char == 'z' or char == 'Z':
            solution.append('Zulu')

        else:
            solution.append(char)

    return ' '.join(solution)


print(to_nato("This"))
