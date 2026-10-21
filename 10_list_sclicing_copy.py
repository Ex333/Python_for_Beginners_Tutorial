numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])  # [20, 30, 40]
print(numbers[:3])   # [10, 20, 30]
print(numbers[2:])   # [30, 40, 50]
print(numbers[::2])  # [10, 30, 50]
print(numbers[::-1]) # [50, 40, 30, 20, 10]

#Now  we gonna do minus indexes like:

numbers = [10, 20, 30, 40, 50]

print(numbers[-1])    # 50
print(numbers[-2])    # 40
print(numbers[-3:])   # [30, 40, 50]
print(numbers[:-1])   # [10, 20, 30, 40]

#Reversing the list:
numbers = [10, 20, 30, 40, 50]

reversed_numbers = numbers[::-1]

print(reversed_numbers)
print(numbers)

#Copying the list (this is v important topic:)

servers = ["web01", "db01", "app01"]

backup = servers    # this is a wrong way! 
backup.append("monitor01")

print(servers)
print(backup)

# The  right way is like: 

servers = ["web01", "db01", "app01"]

backup = servers[:]
backup.append("somethig01")
print(servers)
print(backup)