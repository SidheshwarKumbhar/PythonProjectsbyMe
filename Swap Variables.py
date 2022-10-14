"""-----------------------------------------------------------------------------------------------------------------
* Swapping variables means assigning the value of variable ato variable b and vice versa.
* We have so many algorithms to swap variables but the easiest ones are:
        Swapping two variables by introducing another variable.
        Swapping variables by simply assigning them to each other.
---------------------------------------------------------------------------------------------------------------------"""
# Swapping two variables by introducing another variable

a = 10
b = 20

c = a
a = b
b = c

print("a = ", a)
print("b = ", b)

# Swapping variables by simply assigning them to each other.

a = 100
b = 200

a, b = b, a

print("a = ", a)
print("b = ", b)


