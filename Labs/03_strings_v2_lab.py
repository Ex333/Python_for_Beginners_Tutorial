# String Type Part 2 – LAB

# 1. You work at a Civil Registry Office and use Python. A girl named Kasia, whose maiden name is Sowa, is getting married to a man whose last name is Mrugała. Kasia wants to keep both last names.

# Define the variables firstName, familyName, and lastName and assign them strings corresponding to her first name, maiden name, and new last name. Then create a variable called newName and store the result of concatenating firstName, a space, familyName, another space, and lastName. Print the new full name.

# 2. Define a variable called music with the following content (these are song titles and artists from the movie Minions):

# "Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I'm a Man" Steve Winwood

# Note: This string contains both an apostrophe and quotation marks, so you need to modify the way the string is written using the methods shown in the lesson so that the variable can be defined correctly.

# 3. The text above contains information about three songs. Modify the text so that the second and third songs are displayed on new lines. Again, you need to add special characters presented in the lesson to the string.

# 4. Prepare several print statements that will display the following ASCII art:

# (\(\
# ( -.-)
# O_(")(")

#1
firstName = "Kasia"
familyName = "Sowa"
lastName = "Mrugała"

newName = firstName + " " + familyName + " " + lastName

print(newName)

#2
music = '''"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I'm a Man" Steve Winwood'''

print(music)

#3
music = '''"Universal Fanfare" Jerry Goldsmit \n "Happy Together" Garry Bonner \n"I'm a Man" Steve Winwood'''

print(music)

#4
print("(\\(\\")
print("( -.-)")
print('O_(")(")')