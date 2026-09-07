# 1. Create a variable called "quote" and assign it the following value:
# "A good programmer is someone who always looks both ways before crossing a one-way street"

# 2. Print the text using only uppercase letters.

# 3. Print the text using only lowercase letters.

# 4. Check if the text ends with the word "street".

# 5. Check if the text is written using only uppercase letters.

# 6. Check if the text converted to uppercase is written using only uppercase letters.
#    (Use function/method composition.)

# 7. Find the position (starting from zero) of the substring "one" in the text.

# 8. Replace the substring "one" with "1".

# 9. Replace the substring "one" with "1" and the substring "both" with "2".

# 10. Split the string into smaller strings using a space as the separator.

# 11. Check if the string is a number, a decimal number,
#     a string containing only letters, and a string containing
#     only letters and numbers.

# Note:
# The last task returns four False values.
# The last two results may be surprising.
# Our string contains spaces and consists of multiple words,
# so it is neither an alphabetic string nor an alphanumeric string.

#1
quote = "A good programmer is someone who always looks both ways before crossing a one-way street"

#2
print(quote.upper())

#3
print(quote.lower())

#4
print(quote.endswith("street"))

#5
print(quote.isupper())

#6
print(quote.upper().isupper())

#7
print(quote.find("one"))

#8
print(quote.replace("one", "1"))

#9
print(quote.replace("one", "1").replace("both", "2"))

#10
print(quote.split(sep=" "))

# 11

print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())