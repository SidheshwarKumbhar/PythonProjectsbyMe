"""--------------------------------------------------------------------------------------------------------------------
* Rock Paper Scissors is a hand game usually played between two people. In this game, scissors can beat paper, paper
can beat rock, and rock can beat scissors.
* To create and play rock paper scissors, we will use the if and elif statements in Python. we will prepare
this game to be played between two players. Player-1 will be the user, and player-2 will be the computer. Player
one will manually select the rock paper or scissor, while player two will choose randomly. So I will also use the
random module in Python to create this game.
--------------------------------------------------------------------------------------------------------------------"""
import random

player1 = input("choose between rock, paper and scissors : ").lower()
player2 = random.choice(['rock', 'paper', 'scissor'])
print("system has selected : ", player2)

if player1 == 'paper' and player2 == 'rock':
    print("Congratulation you Won")
elif player1 == 'scissors' and player2 == 'paper':
    print("Congratulation you Won")
elif player1 == "rock" and player2 == 'scissors':
    print("Congratulation you Won")
elif player1 == player2:
    print('game tie')
else:
    print("System Won !!!!!! beater luck next time")
