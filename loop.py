# -----------------------------------------------
# Exercise 1: Using random.choice() with a list
# -----------------------------------------------
import random

COLORS = ["Red", "Blue", "Black", "White", "Purple"]

# Pick a random color from the list
bestColor = random.choice(COLORS)
print("Available colors:", COLORS)

# Loop through each color in the list
for col in COLORS:
    print(f"Checking the {col} varieties")
    if col == bestColor:
        print("##############################")
        print(f"The Best Color {bestColor} is selected")
        print("##############################")
        continue  # Skip to the next iteration
    print("XXXXXXXXXXXXX")
    print("Color search is unsuccessful")
    print("XXXXXXXXXXXXX")
    print(f"{bestColor} is the chosen color after round choices")

# -----------------------------------------------
# Exercise 2: Nested For Loop
# -----------------------------------------------
Town = ("Obigbo", "Eneka", "Awka")

# Loop through each town
for i in Town:
    print(i)
    print(f'{i} might be the town to consider')
    # Nested loop to print each character in the town's name
    for j in i:
        print(j)

print("This is the end of the code")

# -----------------------------------------------
# Exercise 3: While Loop with Time Delay
# -----------------------------------------------
import time

NumberOfWorkers = 1.5
# Infinite loop that increases NumberOfWorkers and prints its value
while True:
    print(f"The value of NumberOfWorkers is {NumberOfWorkers} - we may need more hands")
    print("Looping...")
    NumberOfWorkers += 1
    time.sleep(2)  # Pause for 2 seconds in each iteration

# The code below will never run because of the infinite loop
print("This is the end of the code")

# -----------------------------------------------
# Exercise 4: Random Color with Break
# -----------------------------------------------
import random

COLORS = ["Red", "Blue", "Black", "White", "Purple"]
bestColor = random.choice(COLORS)
print("Available colors:", COLORS)

for col in COLORS:
    print(f"Checking the {col} varieties")
    if col == bestColor:
        print("##############################")
        print(f"The Best Color {bestColor} is selected")
        print("##############################")
        break  # Exit the loop when the best color is found
    print("XXXXXXXXXXXXX")
    print("Color search is unsuccessful")
    print("XXXXXXXXXXXXX")

# -----------------------------------------------
# Exercise 5: Random Color with Continue
# -----------------------------------------------
import random

COLORS = ["Red", "Blue", "Black", "White", "Purple"]
bestColor = random.choice(COLORS)
print("Available colors:", COLORS)

for col in COLORS:
    print(f"Checking the {col} varieties")
    if col == bestColor:
        print("##############################")
        print(f"The Best Color {bestColor} is selected")
        print("##############################")
        continue  # Continue to the next color after finding the best one
    print("XXXXXXXXXXXXX")
    print("Color search is unsuccessful")
    print("XXXXXXXXXXXXX")
    print(f"{bestColor} is the chosen color after round choices")
