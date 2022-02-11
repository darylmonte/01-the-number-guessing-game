"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
import random, time

print(
'''
=======================================
|                                     |
|       GUESS THE SECRET NUMBER       |
|                                     |
=======================================
'''
    )

scores = [] # stores the score of each game

def start_game():

    lower_limit = 1
    upper_limit = 100
    ANSWER = random.randint(lower_limit, upper_limit)

    print(f"I'm thinking of a number between {lower_limit} and {upper_limit}, can you guess what it is?")
    time.sleep(1)

    try:
        guess = int(input(f"Enter a number between {lower_limit} and {upper_limit}: "))
        attempts = 1

        while guess != ANSWER:
            if guess > upper_limit or guess < lower_limit:
                print(f"Try again. My secret number is only between 1 and 100.\n")
            elif guess > ANSWER:
                print(f"Your guess is too high.\n")
            elif guess < ANSWER:
                print(f"Your guess is too low.\n")

            guess = int(input(f"Enter a number between {lower_limit} and {upper_limit}: "))
            attempts += 1
    except ValueError:
        print("\nxXX-- Oh no! That's not a valid number. Let's start again. --XXx\n")
        start_game()
    else:
        print(f"\nFantastic, you got it!!!\nIt took you {attempts} tries to guess the secret number.\n")
        scores.append(attempts)

# Kick off the program by calling the start_game function.
start_game()

play_again = input("Would you like to play again? [y]es/[n]o: ")
while play_again.lower() == "y" or play_again.lower() == "yes":
    # Reference: https://www.geeksforgeeks.org/python-program-to-find-smallest-number-in-a-list/
    if min(scores) == 1:
        print("\nSomeone got lucky and guessed the number in a single attempt. Try your luck...\n")
    else: 
        print(f"\n===> The score to beat is {min(scores)} attempts! <===\n")
    start_game()
    play_again = input("Would you like to play again? [y]es/[n]o: ")


print("Thank you for playing! Ciao!")