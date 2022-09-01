"""---------------------------------------------------------------------------------------------------------------
* The Python programming language provides many inbuilt functions to find the duplicate values,here we will use an
algorithm instead of an inbuilt function.
-------------------------------------------------------------------------------------------------------------------"""


def find_duplicate(x):
    length = len(x)
    duplicate = []
    for i in range(length):
        n = i + 1
        for a in range(n, length):
            if x[i] == x[a] and x[a] not in duplicate:
                duplicate.append(x[a])

    return duplicate


names = ["Aman", "Akanksha", "Divyansha", "Devyansh", "Aman", "Diksha", "Akanksha"]

print(find_duplicate(names))
