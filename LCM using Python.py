"""-----------------------------------------------------------------------------------------------------------------
* Finding LCM of two numbers means finding the smallest number that is a multiple of both the numbers. Python has
 many inbuilt functions that you can use for mathematical calculations, but unfortunately, it does not have any
 function to calculate the LCM of two or more numbers. So for calculating the LCM of two numbers using Python, you
 have to define your Python function.
-------------------------------------------------------------------------------------------------------------------"""


def least_common_multiple(a, b):
    if a > b:
        greater = a
    elif b > a:
        greater = b

    while True:
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        greater = greater + 1
    return lcm


print(least_common_multiple(50, 7))
