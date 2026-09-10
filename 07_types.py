title = "Python"
print(f"{title} is {type(title)}")

version = 3
print(f"{version} is {type(version)}")

is_rainy = True
print(f"{is_rainy} is {type(is_rainy)}")

ratio = 0.33
print(f"{ratio} is {type(ratio)}")
x = 1
y = 1
z = 1
print(x , y, z)

a = b = c = 100  #one line and 3 variables has become value 100
print(a, b, c)
print(id(a), id(b), id(c))  # all three variables have the same memory address

c = c + 1
print(a, b, c)
print(id(a), id(b), id(c))  # c has a different memory address now

c -=1
print(a, b, c)
print(id(a), id(b), id(c))  # c has the same memory address as before

u, v, w = 1, 2, 3
print(u, v, w)
print(id(u), id(v), id(w))  # all three variables have different memory addresses

result = 2 + 2 * 2
print(f"result = {result} is {type(result)}")
result = (2 + 2) * 2
print(f"result = {result} is {type(result)}")
result = 6/2*(1+2)
print(f"result = {result} is {type(result)}") 
result = 4**3**2
print(f"result = {result} is {type(result)}")

x = 12345123123
y = x / 2
print(f"y = {y} is {type(y)}")