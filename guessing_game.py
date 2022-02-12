"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
import random
import time
from statistics import mean
from statistics import median
from statistics import mode

print('''
=======================================
|                                     |
|       GUESS THE SECRET NUMBER       |
|                                     |
=======================================
''')

scores = []  # stores the score of each game


def start_game():

    lower_limit = 1
    upper_limit = 100
    ANSWER = random.randint(lower_limit, upper_limit)
    attempted_numbers = []

    print(f"I'm thinking of a number between {lower_limit} and {upper_limit}, can you guess what it is?")
    time.sleep(0.5)

    try:
        guess = int(input(f"Enter a number between {lower_limit} and {upper_limit}: "))
        attempts = 1
        attempted_numbers.append(guess)

        while guess != ANSWER:
            if guess > upper_limit or guess < lower_limit:
                print("Try again. My secret number is only between 1 and 100.\n")
            elif guess > ANSWER:
                print("Your guess is too high.\n")
            elif guess < ANSWER:
                print("Your guess is too low.\n")

            guess = int(input(f"Enter a number between {lower_limit} and {upper_limit}: "))
            attempts += 1
            attempted_numbers.append(guess)
    except ValueError:
        print("\nxXX-- Oh no! That's not a valid number. Let's start again. --XXx\n")
        start_game()
    else:
        print(f'''
Fantastic, you got it!!!\nIt took you {attempts} tries to guess the secret number.
-----------------
 YOUR GAME STATS
-----------------
Mean: {mean(attempted_numbers)}
Median: {median(attempted_numbers)}
Mode: {mode(attempted_numbers)}
        ''')
        scores.append(attempts)
        time.sleep(2.5)


# Kick off the program by calling the start_game function.
start_game()

play_again = input("Would you like to play again? [y]es/[n]o: ")
while play_again.lower() == "y" or play_again.lower() == "yes":
    if min(scores) == 1:
        print("\nSomebody guessed the number in a single attempt!!! Try beating that...\n")
    else:
        print(f"\n===> The score to beat is {min(scores)} attempts! <===\n")
    start_game()
    play_again = input("Would you like to play again? [y]es/[n]o: ")


print("Thank you for playing! Ciao!")
