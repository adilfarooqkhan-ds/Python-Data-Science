# Python Data Types:
# This file explains the most common built-in data types in Python.

# 1) Numeric Data Types
# Numeric types are used to store numbers.
# Python has three main numeric types:
# - int: whole numbers (positive, negative, or zero)
# - float: numbers with decimal points
# - complex: numbers with a real and imaginary part

# Integer example
age = 25
print("int example:", age, type(age))

# Float example
price = 19.99
print("float example:", price, type(price))

# Complex number example
z = 3 + 4j
print("complex example:", z, type(z))

# Arithmetic operations with numeric types
print("Addition:", 10 + 5)
print("Subtraction:", 10 - 5)
print("Multiplication:", 10 * 5)
print("Division:", 10 / 5)
print("Floor division:", 10 // 3)
print("Modulus:", 10 % 3)
print("Exponentiation:", 2 ** 3)

# 2) Strings
# A string is a sequence of characters enclosed in single quotes, double quotes,
# or triple quotes. Strings are immutable, meaning they cannot be changed once created.

name = "Alice"
message = 'Hello, Python!'
paragraph = """This is a multi-line
string example."""

print("string example:", name, type(name))
print(message)
print(paragraph)

# String operations
print("Length:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Replace:", message.replace("Python", "World"))
print("Concatenation:", "Hello" + " " + "Alice")
print("Slicing:", name[0:3])
print("Character access:", name[1])

# Example of string immutability
# name[0] = 'B'  # This would raise an error because strings are immutable.

# 3) Lists
# A list is an ordered, changeable collection of items enclosed in square brackets [].
# Lists can contain mixed data types and allow duplicates.

numbers = [1, 2, 3, 4, 5]
mixed_list = [10, "aadil", 3.14, True]

print("list example:", numbers, type(numbers))
print("mixed list:", mixed_list)

# List operations
numbers.append(6)
print("After append:", numbers)
numbers.insert(0, 0)
print("After insert:", numbers)
numbers.remove(3)
print("After remove:", numbers)
popped = numbers.pop()
print("Popped item:", popped)
print("List after pop:", numbers)
print("Index 2 value:", numbers[2])
print("Slice:", numbers[1:4])
print("Length:", len(numbers))
print("Sorted list:", sorted(numbers))

# List can also be reversed
numbers.reverse()
print("Reversed list:", numbers)

# 4) Tuples
# A tuple is an ordered, immutable collection of items enclosed in parentheses ().
# Once created, tuple items cannot be changed, added, or removed.

point = (10, 20)
colors = ("red", "green", "blue")
print("tuple example:", point, type(point))
print("colors:", colors)

# Tuple operations
print("Index 0:", point[0])
print("Length:", len(point))
print("Tuple concatenation:", point + (30, 40))
print("Repeated tuple:", colors * 2)

# Tuple cannot be modified
# point[0] = 15  # This would raise an error because tuples are immutable.

# 5) Dictionaries
# A dictionary is an unordered collection of key-value pairs enclosed in curly braces {}.
# Each key is unique and is used to access its corresponding value.

student = {
    "name": "Bob",
    "age": 21,
    "course": "Computer Science"
}
print("dictionary example:", student, type(student))

# Dictionary operations
print("Name:", student["name"])
student["grade"] = "A"
print("After adding grade:", student)
student["age"] = 22
print("After updating age:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Pop age:", student.pop("age"))
print("Dictionary after pop:", student)

# 6) Sets
# A set is an unordered collection of unique items enclosed in curly braces {}.
# Sets do not allow duplicate values and do not support indexing.

set_a = {1, 2, 3, 4, 4, 5}
set_b = {3, 4, 5, 6, 7}
print("set example:", set_a, type(set_a))
print("Duplicate numbers removed:", set_a)

# Set operations
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print("Symmetric difference:", set_a ^ set_b)
set_a.add(8)
print("After add:", set_a)
set_a.remove(1)
print("After remove:", set_a)

# 7) Summary of Python Data Types
# - int: whole numbers
# - float: decimal numbers
# - complex: real + imaginary numbers
# - str: text data
# - list: ordered and mutable collection
# - tuple: ordered and immutable collection
# - dict: key-value pairs
# - set: unique unordered items

# 8) Extra examples for practice
# Example 1: Numeric information
temperature = 36.6
print("Temperature:", temperature)

# Example 2: String information
book_title = "Python for Beginners"
print("Book title:", book_title)
print("First 6 letters:", book_title[:6])

# Example 3: List information
shopping_list = ["milk", "bread", "eggs"]
shopping_list.append("juice")
print("Shopping list:", shopping_list)

# Example 4: Tuple information
date = (2024, 10, 15)
print("Date:", date)

# Example 5: Dictionary information
employee = {"name": "Sara", "salary": 50000, "department": "HR"}
print("Employee:", employee)

# Example 6: Set information
numbers_set = {10, 20, 30, 20, 40}
print("Unique numbers:", numbers_set)

# End of file
print("All data types explained with examples.")
