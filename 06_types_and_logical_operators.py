is_weekend = True
print(f"Is it the weekend? {is_weekend}")

temperature = 5
print(f"Is it cold outside? {temperature < 10}")

is_happy = is_weekend and temperature < 10
print(f"Is it a happy weekend? {is_happy}")

is_happy = not is_weekend and temperature < 10
print(f"Is it a happy weekend? {is_happy}")


# Logical operators
print(True + True)  # equual to 2 
print(bool(100))    #True
print(bool(0))      #False
bool('rain')        #True
bool('')            #False

#Comparison operators
print(10 == 10)         # equal to → True
print(10 != 5)          # not equal to → True

print(10 > 5)           # greater than → True
print(10 < 5)           # less than → False

print(10 >= 10)         # greater than or equal to → True
print(10 <= 5)          # less than or equal to → False
