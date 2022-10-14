"""--------------------------------------------------------------------------------------------------------------------
* Counting occurrences of a character in a string means counting all substrings of a character from the input string.
* To count the occurrences of a character, we need to write an algorithm that returns the number of times each
character appears in the input string. The algorithm must iterate through each character from the beginning to
 count the number of times each character appears in the string.
---------------------------------------------------------------------------------------------------------------------"""


def character_occurrence(string):
    low_string = string.lower()
    counts = {}

    for i in low_string:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    print(counts)


character_occurrence("I am developer,Am i ?")
