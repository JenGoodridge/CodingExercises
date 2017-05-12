# Given a number n, create a method that creates a staircase with n levels.
def staircase(n):
    for lineNumber in range(1, n + 1):
        print((n - lineNumber) * " " + lineNumber * "#")


staircase(3)
