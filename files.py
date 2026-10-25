# Python File Handling - Practice
# Learning how to read and process text files

# 1. Read the whole file

with open("servers.txt", "r") as file:
    content = file.read()

print(content)


# 2. Read only one line

with open("servers.txt", "r") as file:
    content = file.readline()

print(content)


# 3. Read all lines using readline()

with open("servers.txt", "r") as file:
    while True:
        line = file.readline()

        if not line:
            break

        print(line, end="")


# 4. Read all lines using readlines()

with open("servers.txt", "r") as file:
    content = file.readlines()

print(content)


# 5. Count all lines

counter = 0

with open("servers.txt", "r") as file:
    for line in file:
        counter += 1

print(f"Total lines: {counter}")


# 6. Count all words

counter = 0

with open("servers.txt", "r") as file:
    for line in file:
        for word in line.split():
            counter += 1

print(f"Total words: {counter}")


# 7. Count all characters in words

counter = 0

with open("servers.txt", "r") as file:
    content = file.readlines()

    for line in content:
        for word in line.split():
            for letter in word:
                counter += 1

print(f"Total characters: {counter}")


# 8. Count only letters

counter = 0

with open("servers.txt", "r") as file:
    content = file.readlines()

    for line in content:
        for word in line.split():
            for letter in word:
                if letter.isalpha():
                    counter += 1

print(f"Total letters: {counter}")


# 9. Find ERROR messages

with open("servers.txt", "r") as file:
    content = file.readlines()

    for line in content:
        if "error" in line.lower():
            print(line, end="")


# 10. Find stopped servers

with open("servers.txt", "r") as file:
    content = file.readlines()

    for line in content:
        if "stopped" in line.lower():
            print(line, end="")


# 11. Get server name from a string

line = "Server: db02"

server = line.split(":")[1].strip()

print(server)


# 12. Find stopped servers and print server names

server = ""

with open("servers.txt", "r") as file:
    for line in file:
        if line.startswith("Server:"):
            server = line.split(":")[1].strip()

        if "stopped" in line.lower():
            print(f"Server: {server} | {line.strip()}")
