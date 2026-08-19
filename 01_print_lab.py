#1. Display the following text: TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV. Use a single print statement.
#2. Display the above text using the ; character as a separator.
#3. Look at the text below. One part of it is repeated like a chorus in a song... Using a single print statement, display the entire text, 
# but try to shorten the statement. The "chorus" — the repeated part — should appear only once in the print statement. 
# Do you have an idea how to do this?

# I like computers but better is TVP1 but better is TVP2 but better is TVN but better is Polsat but better is BBC but better is HBO but better is MTV

#4. Declare variables ProgramName with the value 'BBC', Item with the value 'News', and Time with the value '18:00'.

#5Note: In this task, do not use string concatenation (joining strings). Use only the print statement!
#Display the following text (pay attention to the period at the end!):
#I like watching News at 18:00 on BBC .

#6. Change the text so that the period is directly after BBC. We still do not use concatenation, but only a single print statement.

#1 
print('TVP1', 'TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', 'MTV', sep='\n')

#2
print('TVP1', 'TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', 'MTV', sep=';')

#3
print("I like computers " + " but better is ".join(["TVP1", "TVP2", "TVN", "Polsat", "BBC", "HBO", "MTV"]))

#4
programname = 'BBC'
item = 'News'
time = '18:00'

#5
print(f"I like watching {item} at {time} on {programname} .")

#6
print(f"I like watching {item} at {time} on {programname}.")
