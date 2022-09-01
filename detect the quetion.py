"""-----------------------------------------------------------------------------------------------------------------
*To write a Python program to detect whether a sentence is a question or not, we first need to create a list
of words that we see at the start of an interrogative sentence. For example, what is your name? where do you live?,
in these two questions, “what” and “where” are the types of words we need to store in a python list. Next, to
check if a sentence is a question or not, we need to check if any word from the list is present at the beginning
of the sentence. If it is present, then the sentence is a question, and if it is not present, then the sentence is
not a question.
---------------------------------------------------------------------------------------------------------------------"""

question_words = ["what", "why", "when", "where", "name", "is", "how", "do", "does", "which", "are", "could", "would",
                  "should", "has", "have", "whom", "whose", "don't"]

sentence = input("enter the your sentence :")
sentence.lower()
sentence_words = list(sentence.split(" "))

if sentence_words[0] in question_words:
    print("this is the question....")
else:
    print("this is the sentence....")
