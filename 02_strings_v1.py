filename = "december_production_report.xlsx"

is_excel = filename.endswith(".xlsx")
is_word = filename.endswith(".docx")
print("*" * 30)
print("The file:", filename)
print("*" * 30)
print("is_excel:", is_excel)
print("*" * 30)
print("is_word:", is_word)
print("*" * 30)

print(1 + 2)
print("1" + "2")
# print("1" + 2)  # TypeError: cannot add a string and an integer

print("*" * 30)

print("10aaA".isalnum())  # Check if the string contains only letters and numbers

print("*" * 30)

print("aaa".isalpha())  # Check if the string contains only letters

print("*" * 30)

print("ĄĘ".isascii())  # Check if the string contains only ASCII characters

print("*" * 30)

print("2".isdigit())  # Check if the string contains only digits

print("*" * 30)

print("2.5".isnumeric())  # Check if the string contains only numeric characters

print("*" * 30)

print(" ".isspace())  # Check if the string contains only whitespace

print("*" * 30)

print("is lower".islower())  # Check if all letters are lowercase

print("*" * 30)

print("IS UPPER?".isupper())  # Check if all letters are uppercase

print("*" * 30)

print("Continent Europe".istitle())  # Check if each word starts with an uppercase letter

print("*" * 30)

continent = "Europe"

print(continent.upper())  # Convert to uppercase
print(continent.lower())  # Convert to lowercase
print(continent.title())  # Convert to title case