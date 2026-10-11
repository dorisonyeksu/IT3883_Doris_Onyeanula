
# Assignment3.py
# IT3883/Section 01
# Doris Onyeanula
# Assignment Number: Assignment 3
# 10/10/26
# Purpose: This program converts miles per gallon (MPG) into
# kilometers per liter (KM/L). The result updates automatically
# when the user types a value. It also handles invalid input.
# Resources Used: Python Tkinter documentation

# Import Tkinter to create the application window and GUI elements.
import tkinter as tk

# Creates the main application window.
window = tk.Tk()
window.title("MPG to KM/L Converter")
window.geometry("380x250")
window.resizable(False, False)

# Store the user's input and the converted result.
mpg_input = tk.StringVar()
result_text = tk.StringVar(value="Enter a number to begin.")

# This function converts the input and handles invalid entries.
def convert_mpg(*args):
    entered_value = mpg_input.get().strip()

    # Handle an empty input box.
    if entered_value == "":
        result_text.set("Enter a number to begin.")
        return

    try:
        # Convert the input to a number.
        mpg_value = float(entered_value)

        # Apply the conversion formula from the assignment.
        km_per_liter = mpg_value * 0.425143707

        # Display the answer rounded to two decimal places.
        result_text.set(f"{km_per_liter:.2f} km/L")

    except ValueError:
        # Show a message instead of crashing on letters.
        result_text.set("Please enter a valid number.")

# Add a heading to the window.
heading = tk.Label(
    window,
    text="MPG to KM/L Converter",
    font=("Arial", 16, "bold")
)
heading.pack(pady=15)

# Add a label and input box for miles per gallon.
input_label = tk.Label(window, text="Miles per Gallon (MPG):")
input_label.pack()

input_box = tk.Entry(
    window,
    textvariable=mpg_input,
    font=("Arial", 12),
    justify="center"
)
input_box.pack(pady=8)

# Add a label to display the converted result.
result_label = tk.Label(
    window,
    textvariable=result_text,
    font=("Arial", 12, "bold")
)
result_label.pack(pady=10)

# Run the conversion function whenever the input changes.
mpg_input.trace_add("write", convert_mpg)

# Keep the application window open.
window.mainloop()
