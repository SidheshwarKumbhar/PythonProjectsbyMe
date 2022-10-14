"""-----------------------------------------------------------------------------------------------------------------
* A pyramid pattern is like a triangle that is not empty, so to create such a pattern using Python we need
 to use for loops to design a pyramid structure using stars, numbers, alphabets, or any other symbol
--------------------------------------------------------------------------------------------------------------------"""

def pyramid_pattern(n):
    for i in range(0, n):
        for j in range(0, n):
            print(end=" ")

        n -= 1
        for j in range(0, i+1):
            print("+", end=" ")
        print("\r")


pyramid_pattern(10)


