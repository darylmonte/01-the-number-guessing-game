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

scores = [10]  # stores the score of each game, default high score is 10
lower_limit = 1
upper_limit = 100

print('''
=======================================
|                                     |
|       GUESS THE SECRET NUMBER       |
|                                     |
=======================================
''')
print(f"I'm thinking of a number between {lower_limit} and {upper_limit}, can you guess what it is?\n")
time.sleep(0.3)


def start_game():

    ANSWER = random.randint(lower_limit, upper_limit)
    attempted_numbers = []

    try:
        guess = int(input(f"Enter a number between {lower_limit} and {upper_limit}: "))
        attempts = 1
        attempted_numbers.append(guess)

        while guess != ANSWER:
            if guess > upper_limit or guess < lower_limit:
                print(f"Try again. My secret number is only between {lower_limit} and {upper_limit}.\n")
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
Mean: {round(mean(attempted_numbers), 2)}
Median: {median(attempted_numbers)}
Mode: {mode(attempted_numbers)}
        ''')
        scores.append(attempts)
        time.sleep(1.5)


play_again = 'y'
while play_again.lower() == "y" or play_again.lower() == "yes":
    start_game()
    play_again = input("Would you like to play again? [y]es/[n]o: ")
    if min(scores) == 1:
        print("\nSomebody guessed the number in a single attempt!!! Try beating that...\n")
    elif play_again.lower() == "y" or play_again.lower() == "yes":
        print(f"\n===> The score to beat is {min(scores)} attempts! <===\n")
        time.sleep(2)
    else:
        print("\nThank you for playing! Ciao!\n")
        break
