# Python Exercise

# 1. Did you know that the creator of the Python programming language, Guido van Rossum, was a fan of the comedy group Monty Python? Yes! That is where the name of the language came from.

# Go to the Wikipedia page about Monty Python:

# Monty Python – Wikipedia

# Copy the text from the paragraph titled "Monty Python".

# 2. In your script, create a variable called article and assign the copied text to it.

# Note: The copied text is long and contains line breaks. If you want to assign such a text to a variable, you can use three quotation marks:

# article = '''
# long text and even
# longer text...
# '''
# 3. Convert the text to uppercase and display it. Do this in one statement.
# 4. Display the text replacing 'monty' with 'flying'. Since Python distinguishes between lowercase and uppercase letters, convert the text to lowercase before replacing it. Again, try to do this in one statement.
# 5.Split the text into words based on spaces and display the resulting list.
# 6.Display the text in the following format:
# word python appears 3 times

# Of course, the number 3 should be calculated as the number of occurrences of the word python in the article variable.

# 7.Using print, display exactly:
# to print the \ you need to put \ twice in your text like this: \\
# 8.Using print, display:
# The best hits of '80s!!!

# Do this in two ways:

# First, enclose the text in single quotes '.
# Second, enclose the text in double quotes ".
# 9.Now create a mini currency exchange calculator.

# We want to display a table like this:

# cur    exchange    amount
# USD    3.65        64.10958904109589
# EUR    4.23        55.31914893617021

# To do this:

# First, declare a variable amountPLN and assign it the value 234.
# Then display the text using tabs (\t) to make the output look like a table. Use several print statements — a single-line print would be too difficult to understand at this stage.
# Calculate the values in the amount column by dividing amountPLN by the current USD and EUR exchange rates. In this example, the rates are 3.65 and 4.23.
# 10. Declare a variable ValueAsText and assign it the value:
# '123.45'
# 11. Declare a variable factor with the value:
# 1.23
# 12.Display the following text:
# value is 123.45 factor is 1.23 value*factor= 151.8435

# When calculating value * factor, convert ValueAsText to the float

#Answers!!
#1
'''https://en.wikipedia.org/wiki/Monty_Python'''

#2
article = '''
Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy group who created their sketch comedy show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and impact, including touring stage shows, films, numerous albums, several books, and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Their sketch show has been referred to as "not only one of the more enduring icons of 1970s British popular culture, but also an important moment in the evolution of television comedy".[7]
Broadcast by the BBC between 1969 and 1974, Monty Python's Flying Circus was conceived, written, and performed by its members Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. Loosely structured as a sketch show, but with an innovative stream-of-consciousness approach, aided by Gilliam's animation, it pushed the boundaries of what was acceptable in style and content.[8][9] A self-contained comedy team responsible for both writing and performing their work, the Pythons had creative control which allowed them to experiment with form and content, discarding rules of television comedy. Following their television work, they began making films, which include Monty Python and the Holy Grail (1975), Life of Brian (1979) and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while in North America, it has coloured the work of cult performers from the early editions of Saturday Night Live through to more recent absurdist trends in television comedy. "Pythonesque" has entered the English lexicon as a result.
In a 2005 poll of over 300 comics, comedy writers, producers and directors throughout the English-speaking world to find "The Comedian's Comedian", three of the six Pythons members were voted to be among the top 50 greatest comedians ever: Cleese at No. 2, Idle at No. 21, and Palin at No. 30.[10][11]
'''
#3
print(article.upper())

#4
print(article.lower().replace("monty", "flying"))

#5
print(article.split(" "))

#6
print(f"The Word python appears in this text a {article.count('python')} times ")

# 7
print("to print the \\ you need to put \\ twice in your text like this: \\")


# 8
print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")


# 9
amountPLN = 234

print("cur", "\texchange", "\tamount")
print("USD", "\t3.65", "\t", amountPLN / 3.65)
print("EUR", "\t4.23", "\t", amountPLN / 4.23)


# 10
ValueAsText = '123.45'


# 11
factor = 1.23


# 12
print(
    "value is", ValueAsText,
    "factor is", factor,
    "value*factor=", float(ValueAsText) * factor
)
