"""==================================================================================================================
* The Quiz game asks the player questions about animals. They have three chances to answer each question.Each correct
 answer will score a point. At the end of the game, the program will reveal the player’s final score.
===================================================================================================================="""


def guess_animal(ans, guess):
    global score
    still_guess = True
    attempt = 0
    while still_guess and attempt < 3:
        if ans == guess:
            print("Your Answer is Correct.")
            score += 1
            still_guess = False

        else:
            if attempt < 2:
                guess = input("Your Answer is Wrong,Try again...")
            attempt += 1

    if attempt == 3:
        print("The correct answer is", ans)


score = 0
print("Guess the Animal..")
your_guess = input("Which is the fastest land animal....?")
guess_animal("cheetah", your_guess)

print("your score is {}".format(score))
