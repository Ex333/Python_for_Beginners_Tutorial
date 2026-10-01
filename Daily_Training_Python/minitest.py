from random import randint
from art import text2art

print(text2art("GUESS THE NUMBER    1- 10"))

number_to_guess = randint(1, 10)

guessed = -1
tries = 4
attempts = 0

while guessed != number_to_guess and tries > 0:

    guessed = int(input("Guess the number!: "))
    attempts += 1
    tries -= 1

    if guessed == number_to_guess:
        print(f"Congratulations! You guessed it in {attempts} attempt(s)!")

    elif guessed < number_to_guess:
        print("Too low!")

    else:
        print("Too high!")

    print(f"Tries left: {tries}")