# ---------------------------
# Writing of Function Code Examples
# ---------------------------

# Example 1: Function that returns the difference between gain and expenses
def commission(gain, expenses):
    total = gain - expenses
    return total

myGain = commission(18090, 5786)
print(myGain)  # Output: 12304

# -------------------------------------------------

# Example 2: Function that prints difference (instead of returning it)
def commission(gain, expenses):
    difference = gain - expenses
    print(difference)

print(commission(200, 150))  # Output: 50 then None (because print() returns nothing)

# -------------------------------------------------

# Example 3: Function to sum numbers in a list using *args logic
def sum(args):
    x = 0
    for i in args:
        x = x + i
    return x

out = sum([100, 250, 290])  # Output: 640
print(out)

# -------------------------------------------------

# Default Argument Example
# Demonstrates how to provide a default value for function parameters
def greetings(MSG="Morning"):
    print(f"Good {MSG} everyone")
    print("Welcome to Pie function")

greetings()              # Uses default: "Morning"
greetings("Afternoon")   # Overrides default

# -------------------------------------------------

# Order of Arguments + Conditional Logic
# Demonstrates using keyword arguments and conditional logic with if-elif-else
def result(name, score):
    print(f"Hello {name}, this is your score {score}")
    if score >= 50 and score < 70:
        print("You crossed but need more efforts next term")
    elif score >= 71 and score <= 90:
        print("Congratulations, you came out with flying colors")
    elif score >= 91 and score <= 100:
        print("Congratulations, you came out with flying colors and you will receive a scholarship")
    else:
        print("Study harder for next semester")

# Function calls
# result("Chidi", 80)
# result("Edu", 65)
# user_name = input("Enter your name: ")
# user_score = int(input("Enter your score: "))
result(score=80, name="Ifeanyi")

# -------------------------------------------------

# Variable-Length Argument: *args (Non-keyword)
# Demonstrates handling multiple positional arguments
def order_drinks(min_order, *args):
    print(f"You ordered {min_order} drinks")
    for item in args:
        print(f"You ordered {item} drinks")
    print("Your drinks will be delivered in half an hour time")
    print("Enjoy your time here")

order_drinks("Gulder", "Desperado", "Yougurt")

# -------------------------------------------------

# Variable-Length Arguments: *args and **kwargs
# Simulates a random activity scheduler using both positional and keyword arguments

import random

def time_activity(*args, **kwargs):
    print(args)     # Prints all positional arguments as a tuple
    print(kwargs)   # Prints all keyword arguments as a dictionary

    # Random total time based on input minutes and a random addition
    min = sum(args) + random.randint(0, 60)
    print(min)

    # Randomly select one activity from kwargs
    choice = random.choice(list(kwargs.keys()))
    print(choice)

    # Display chosen activity and assigned time
    print(f"You have to spend {min} minutes for {kwargs[choice]}")

# Call the function with example arguments
time_activity(10, 20, 10, hubby="Gaming", sports="football", work="DevOps")
