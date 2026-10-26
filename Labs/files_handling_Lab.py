with open("servers.txt", "r", encoding="utf-8") as file:
    for line in file:
        for word in line.split():
            print(word)
            print(type(word))