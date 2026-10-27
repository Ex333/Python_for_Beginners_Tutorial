with open("servers.txt", "r", encoding="utf-8") as file:
    content = file.readlines()
    for line in content:
        for word in line.split():
            print(type(word))
            print(type(content))