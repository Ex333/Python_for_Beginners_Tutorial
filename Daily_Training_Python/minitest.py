from random import randint
from datetime import datetime

time = datetime.now()
time = time.strftime("%H:%M:%S")
number = randint(1, 10)
tries = 3
guessed_number = -1

print("WELCOME IN MY GAME! You must guess the number in range 1-10, have fun and you have only 3 tries...")
name = input("what is your name:")

print(f"let's begin! {name} our jurney u started at: {time}!")

while guessed_number == number or tries == 0:
    pass