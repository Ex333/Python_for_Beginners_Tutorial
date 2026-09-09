# ### Python Exercise – Variables, String Formatting and Division

# 1. Declare a variable `name` and assign your name to it.

# 2. Declare a variable `age` and assign your age to it.

# 3. Declare a variable `daysInYear` and assign the value `365` to it.

# 4. Declare a variable `message` and assign it the following value.
#    **Note:** Replace `???` with the appropriate formatting placeholders that allow you to display a string and two numbers:

# ```python
# '??? is ??? years old, so is about ??? days old'
# ```

# 5. Display the following information using string formatting:

# ```text
# Jan is 26 years old, so is about 9490 days old
# ```

# 6. Change the `name` and `age` variables and display the message again using the **same instruction as before**.

# 7. Change the value of the `message` variable to:

# ```python
# message = '{???} is {???} years old, so is about {???} days old'
# ```

# Again, replace `???` with the appropriate formatting placeholders that allow you to display a string and two numbers.

# 8. Using the `format()` method with the `message` variable, display the following message:

# ```text
# Chris is 17 years old, so is about 6205 days old
# ```

# 9. Calculate the **integer quotient** and the **remainder** when dividing `1234567890` by `12345`.

# The result should look like this:

# ```text
# 1234567890 divided by 12345 is 100005 and the remainder is 6165
# ```

#ANSWERSSSS
#1
name = "Mateusz"

#2
age = 36

#3
daysInYear = 365

#4
message = f'{name} is {age} years old, so is about {age * daysInYear} days old'
print(message)

#5
name = "Jan"
age = 26
print(f'{name} is {age} years old, so is about {age * daysInYear} days old')

#6
name = "Chris"
age = 17
print(f'{name} is {age} years old, so is about {age * daysInYear} days old')

#7
message = '{0} is {1} years old, so is about {2} days old'

#8
print(message.format("Chris", 17, 17 * daysInYear))

#9
number = 1234567890
divisor = 12345

quotient = number // divisor
remainder = number % divisor

print(f'{number} divided by {divisor} is {quotient} and the remainder is {remainder}')