"""-------------------------------------------------------------------------------------------------------------
* Finding the missing number in an array means finding the numbers missing from the array according to the
range of values inside the array.
* To find the missing number in an array, we need to iterate over the input array and store the numbers in
 another array that we did not find in the input array while iterating over it.
-----------------------------------------------------------------------------------------------------------------"""

def missingNumber(n):
    length = len(n)
    missedNumber = []
    for i in range(1, 1 + length):
        if i not in n:
            missedNumber.append(i)
    return missedNumber


listOfNumber = [1, 2, 3, 5, 6, 7, 9, 10]

print("the missed number is :", missingNumber(listOfNumber))
