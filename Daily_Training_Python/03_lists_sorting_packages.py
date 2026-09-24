numbers = [4, 7, 2, 9, 6, 11]

# 1. Print every number
for number in numbers:
    print(number)


# 2. Print numbers bigger than 5
for number in numbers:
    if number > 5:
        print(number)


# 3. Print even numbers
for number in numbers:
    if number % 2 == 0:
        print(number)


# 4. Print index of every number
for index in range(len(numbers)):
    print(index)


# 5. Print index and number
for index in range(len(numbers)):
    print(index, numbers[index])


# 6. Check if number is even or odd
for number in numbers:
    if number % 2 == 0:
        print(f"number {number} is even")
    else:
        print(f"number {number} is odd")


# 7. enumerate() - index + number
for index, number in enumerate(numbers):
    print(index, number)


# 8. enumerate() + condition
for index, number in enumerate(numbers):
    if number > 5:
        print(index, number)