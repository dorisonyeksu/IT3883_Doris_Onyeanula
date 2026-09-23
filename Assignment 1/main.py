# Program Name: Assignment1.py
# Course: IT3883/Section 01
# Student Name: Doris Onyeanula
# Assignment Number: Lab #1
# Due Date: 09/22/2026
# Purpose: This program displays a text based menu that allows the user
# to append text to a buffer, clear the buffer, display the
# current contents of the buffer, or exit the program.

# Resources Used:
# - Module 1
# - Python Documentation (https://docs.python.org)

# store user input
buffer = ""

# keep the program running
running = True

# Main program loop
while running:

    # Display menu options
    print("\n----- MENU -----")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Get user's choice
    choice = input("Enter your choice (1-4): ")

    # Option 1: Append text to the buffer
    if choice == "1":
        text = input("Enter text to add: ")
        buffer += text
        print("Text added to buffer.")

    # Option 2: Clear the buffer
    elif choice == "2":
        buffer = ""
        print("Buffer has been cleared.")

    # Option 3: Display the buffer
    elif choice == "3":
        print("\nCurrent Buffer Contents:")
        print(buffer)

    # Option 4: Exit the program
    elif choice == "4":
        print("Exiting program...")
        running = False

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")