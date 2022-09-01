"""-----------------------------------------------------------------------------------------------------
* In the number guessing game, the program selects a random number between two numbers, and the user
  guesses the correct number.
*To create a guessing game, we need to write a program to select a random number between 1 and 10.
 To give hints to the user, we can use conditional statements to tell the user if the guessed number
 is smaller, greater than or equal to the randomly selected number.
-------------------------------------------------------------------------------------------------"""

import random

n = random.randrange(1, 10)
guess = int(input("Enter your guessed number between 1 to 10 : "))

while n != guess:
    if n > guess:
        print("guessed number is too small")
        guess = int(input("Enter number again : "))

    elif n < guess:
        print("guessed number is too large")
        guess = int(input("Enter number again : "))

    else:
        break


print("Congratulation your guessed number is correct!!!!!")
