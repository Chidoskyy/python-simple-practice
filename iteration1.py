#Write a program which repeatedly reads integers until the user enters
#“done”. Once “done” is entered, print out the total, count, and average of the
#integers. If the user enters anything other than a integers, detect their mistake
#using try and except and print an error message and skip to the next integers.

def calculate_average():
    total = 0
    count = 0

    while True:
        user_input = input("Enter an integer or 'done' to finish: ")

        if user_input.lower() == 'done': 
            break

        try:
            num = int(user_input)
            total += num
            count += 1
        except ValueError:
            print("Error: Invalid input.Please enter an integer.")

    if count == 0:
        
        print("No integers entered.")
    else:
        avearage = total / count
        print(f"Total: {total}")
        print(f"Count: {count}")
        print(f"Average: {average:2f}")
calculate_average()
