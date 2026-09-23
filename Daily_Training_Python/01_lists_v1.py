# ZIP IN PYTHON

servers = [
    "web-01",
    "web-02",
    "db-01",
    "db-02",
    "backup-01"
]

server_status = [
    "online",
    "offline",
    "online",
    "online",
    "offline"
]

for server, status in zip(servers, server_status):
    if status == "offline":
        print(f"{server} is offline")
    else:
        print(f"{server} is online")


# ZIP WITH TWO LISTS

names = [
    "Matt",
    "Anna",
    "John",
    "Tom"
]

ages = [
    36,
    25,
    30,
    28
]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


# ZIP WITH PRODUCTS AND PRICES

products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]

prices = [
    1200,
    50,
    80,
    300
]

for product, price in zip(products, prices):
    print(f"{product}: {price} EUR")


# CONVERT ZIP TO A LIST

countries = [
    "Germany",
    "Poland",
    "Spain"
]

capitals = [
    "Berlin",
    "Warsaw",
    "Madrid"
]

result = list(zip(countries, capitals))

print(result)


# ZIP WITH DIFFERENT LENGTH LISTS

employees = [
    "Matt",
    "Anna",
    "John",
    "Tom"
]

departments = [
    "IT",
    "HR"
]

for employee, department in zip(employees, departments):
    print(f"{employee} works in {department}")


# ZIP LONGEST

from itertools import zip_longest

employees = [
    "Matt",
    "Anna",
    "John",
    "Tom"
]

departments = [
    "IT",
    "HR"
]

for employee, department in zip_longest(
    employees,
    departments,
    fillvalue="unknown"
):
    print(f"{employee} works in {department}")


# ZIP LONGEST WITH SERVERS

servers = [
    "web-01",
    "web-02",
    "db-01",
    "db-02"
]

status = [
    "online",
    "offline"
]

for server, server_status in zip_longest(
    servers,
    status,
    fillvalue="unknown"
):
    print(f"{server}: {server_status}")