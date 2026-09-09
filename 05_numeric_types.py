# ==========================================
# PYTHON - NUMBERS AND BASIC OPERATORS
# ==========================================


# ------------------------------------------
# MULTIPLICATION
# ------------------------------------------

print(5 * 3)

three = 3
five = 5

print(five * three)

print(type(five))


# ------------------------------------------
# DIVISION
# ------------------------------------------

new_value = five / three

print(new_value)

print(type(new_value))
# / always returns float


# ------------------------------------------
# sys.maxsize
# ------------------------------------------

import sys

print(sys.maxsize)

# sys.maxsize is NOT the maximum value of an int.
# It is the maximum size used for things like indexes
# and some system-related limits.


# ------------------------------------------
# VERY BIG INTEGER
# ------------------------------------------

very_big_value = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

print(type(very_big_value))

very_big_value += 1

print(very_big_value)

# Python can handle very big integers.
# int does not have a small fixed maximum value like
# some other programming languages.


# ------------------------------------------
# BIG INTEGER / FLOAT
# ------------------------------------------

smaller_big_value = very_big_value / 2

print(smaller_big_value)

# / converts the result to float.
# Very large floats can be displayed using scientific notation.
#
# Example:
# 5e+87 = 5 * 10^87


# ------------------------------------------
# FLOAT PRECISION
# ------------------------------------------

print(0.1 + 0.2)

# You might expect:
# 0.3
#
# But Python prints:
# 0.30000000000000004
#
# This happens because floats are stored in binary
# and some decimal numbers cannot be represented exactly.


# ------------------------------------------
# DIVISION
# ------------------------------------------

print(10 / 3)

# / = normal division
# Result is always float
#
# 10 / 3 = 3.3333333333333335


# ------------------------------------------
# FLOOR DIVISION
# ------------------------------------------

print(10 // 3)

# // = floor division
#
# 10 // 3 = 3
#
# It removes the decimal part for positive numbers.


# ------------------------------------------
# MODULO / REMAINDER
# ------------------------------------------

print(10 % 3)

# % = remainder
#
# 10 % 3 = 1
#
# Because:
# 10 = 3 * 3 + 1


# ==========================================
# BASIC OPERATORS
# ==========================================


# ------------------------------------------
# ADDITION
# ------------------------------------------

print(5 + 3)

# + = addition
#
# 5 + 3 = 8


# ------------------------------------------
# SUBTRACTION
# ------------------------------------------

print(5 - 3)

# - = subtraction
#
# 5 - 3 = 2


# ------------------------------------------
# MULTIPLICATION
# ------------------------------------------

print(5 * 3)

# * = multiplication
#
# 5 * 3 = 15


# ------------------------------------------
# DIVISION
# ------------------------------------------

print(5 / 2)

# / = division
#
# 5 / 2 = 2.5


# ------------------------------------------
# FLOOR DIVISION
# ------------------------------------------

print(5 // 2)

# // = floor division
#
# 5 // 2 = 2


# ------------------------------------------
# REMAINDER
# ------------------------------------------

print(5 % 2)

# % = remainder
#
# 5 % 2 = 1


# ------------------------------------------
# POWER
# ------------------------------------------

print(5 ** 2)

# ** = power
#
# 5 ** 2 = 25
#
# This means:
# 5 * 5 = 25


# ==========================================
# NEGATIVE POWER
# ==========================================

print(2 ** 3)

# 2 ** 3 = 8
#
# 2 * 2 * 2 = 8


# ==========================================
# INFINITY
# ==========================================

infinity_plus = float("inf")

print(infinity_plus)

# float("inf") = positive infinity

print(infinity_plus + 100)

print(infinity_plus * 2)

# Infinity is bigger than any normal finite float.


# ==========================================
# OPERATOR SUMMARY
# ==========================================

# +   addition
# -   subtraction
# *   multiplication
# /   division
# //  floor division
# %   remainder / modulo
# **  power


# ==========================================
# EXAMPLES
# ==========================================

a = 10
b = 3

print(a + b)     # 13
print(a - b)     # 7
print(a * b)     # 30
print(a / b)     # 3.3333333333333335
print(a // b)    # 3
print(a % b)     # 1
print(a ** b)    # 1000