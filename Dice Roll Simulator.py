"""------------------------------------------------------------------------------------------------------------------
* The Dice Roll Simulation can be done by choosing a random integer between 1 and 6 for which we can use the
 random module.

-----------------------------------------------------------------------------------------------------------------------"""
# importing module for random number

import random

roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print("Rolling again........")
    print("The value are: ")

    print(random.randint(1, 6))

    roll_again = input("Roll Dice again ? ")

