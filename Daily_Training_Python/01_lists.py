# Create a list with servers
servers = ["web01", "web02", "db01"]


# append() adds an element to the end of the list
servers.append("backup01")


# insert() adds an element at a specific index
servers.insert(0, "firewall01")

print(servers)


# while checks the condition again and again
# remove() removes the specified value from the list
# This removes all occurrences of db01
while "db01" in servers:
    servers.remove("db01")

print(servers)


# pop() removes the last element from the list
# The removed element can be saved in a variable
removed_server = servers.pop()

print(f"Removed server: {removed_server}")
print(servers)


# in checks if an element exists in the list
print("web02" in servers)


# index() finds the index of an element
print(servers.index("web02"))


# del removes an element using its index
del servers[1]

print(servers)


# sort() sorts the list in ascending order
servers.sort()

print(servers)


# reverse() reverses the order of the list
servers.reverse()

print(servers)


# enumerate() gives us the index and the element
for number, element in enumerate(servers):
    print(number, element)

