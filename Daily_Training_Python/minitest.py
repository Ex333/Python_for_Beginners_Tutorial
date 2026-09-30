from random import randint
from datetime import datetime

time = datetime.now()
time = time.strftime("%H:%M:%S")
number = randint(1, 10)
tries = 3
guessed_number = -1

print("WELCOME IN MY GAME! You must guess the number in range 1-10, have fun and you have only 3 tries...")
name = input("what is your name:")

# while not name.isalpha():
#     print("name can contain only letters!")
#     name = input("what is your name:") 

# print(f"let's begin! {name} our jurney u started at: {time}!")

# while guessed_number != number and tries > 0:
#     pass

# password = input("enter your password!")

# while len(password) < 8:
#     print("password lenght musst be at least 8 charakters!")
#     password = input("enter your password!")

#validacja imienia

tries = 0

while tries < 3:
    age = int(input("Enter your age: "))

    if 18 <= age <= 100:
        print("Correct!")
        break

    print("Wrong age!")
    tries += 1