# Number Guessing Game

import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20.")
guess = None

# Keep asking until the guess is correct
while guess != secret_number:
    guess = int(input("Take a guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("You got it! The number was", secret_number)
