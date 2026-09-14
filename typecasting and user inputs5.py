"""Typecasting and user inputs in Python.

Typecasting (type conversion) means changing a value from one data type to
another, such as converting text to an integer.
"""

# Common typecasting examples
text_number = "25"
number = int(text_number)          # str -> int
decimal_number = float("3.14")     # str -> float
text = str(100)                    # int -> str
truth_value = bool(1)              # int -> bool (non-zero is True)

print("Integer:", number)
print("Float:", decimal_number)
print("String:", text)
print("Boolean:", truth_value)

# User input
# input() always returns a string, so convert it when a number is required.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))

print(f"Hello, {name}!")
print(f"You are {age} years old and {height} m tall.")

# Example calculation using converted input values
next_year_age = age + 1
print(f"Next year, you will be {next_year_age}.")

# Safe conversion: handle invalid numeric input without stopping the program.
try:
    value = float(input("Enter a number: "))
    print("You entered:", value)
except ValueError:
    print("That is not a valid number.")