# -----------------------------------------------
# String Methods
# -----------------------------------------------

# Define a string
instructions = "deply the artifact to ec2 server in north virginia"
print(instructions)  # Print the original string
print(instructions.capitalize())  # Capitalize the first character of the string

# -----------------------------------------------
# dir() function (shows all available methods for a data type)
# The below block is commented out with triple quotes to prevent execution
# Uncomment to see the list of available methods for each data type
"""
print(dir(instructions))  # Methods for strings
print(dir(""))            # Methods for an empty string
print(dir([]))            # Methods for a list
print(dir(()))            # Methods for a tuple
print(dir({}))            # Methods for a dictionary
"""
# -----------------------------------------------

# Convert the string to uppercase
print(instructions.upper())

# Check if all characters are lowercase (returns True/False)
print(instructions.islower())

# Check if all characters are uppercase (returns True/False)
print(instructions.isupper())

# Find the starting index of the word 'virginia' in the string
print(instructions.find('virginia'))

# Slice a substring from index 42 to 50
print(instructions[42:50])

# Try to find the word "Good" (will return -1 since it's not present)
print(instructions.find("Good"))

# -----------------------------------------------
# Join method - converts elements of a tuple into a single string
# -----------------------------------------------
age = ("17", "28", "11", "44")
print(age)  # Print original tuple
print(".".join(age))  # Join elements with a dot separator
print(">".join(age))  # Join elements with '>'
print("+".join(age))  # Join elements with '+'

# -----------------------------------------------
# List Operations
# -----------------------------------------------
footballTeams = ["arsenal", "Real Madrid", "Liverpool", "Napoli"]
print(footballTeams)  # Print the original list

# Append adds a single new item to the end of the list
footballTeams.append("Barcelona")
print(footballTeams)

# Extend adds multiple items (iterables) to the list
footballTeams.extend(["Chlsea", "Salzburg"])
print(footballTeams)

# Insert a new item at a specific position (index 4 here)
footballTeams.insert(4, "Chicago")
print(footballTeams)

# Pop removes an element at a specific index (default is the last element)
footballTeams.pop(2)  # Removes the element at index 2 (Liverpool)
print(footballTeams)

# The below line is commented because pop() does not accept a value, only an index
# print(footballTeams.pop("Barcelona"))
