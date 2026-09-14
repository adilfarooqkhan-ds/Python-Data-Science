# Arithmetic operators
# + : Adds two values
# - : Subtracts the second value from the first
# * : Multiplies two values
# / : Divides two values and returns a float
# // : Divides and returns the integer part (floor division)
# % : Returns the remainder of division
# ** : Raises a number to a power

print("Arithmetic Operators")
a = 10
b = 3
print("a + b =", a + b)      # 13
print("a - b =", a - b)      # 7
print("a * b =", a * b)      # 30
print("a / b =", a / b)      # 3.3333333333333335
print("a // b =", a // b)     # 3
print("a % b =", a % b)      # 1
print("a ** b =", a ** b)    # 1000
print()

# Comparison operators
# == : Equal to
# != : Not equal to
# >  : Greater than
# <  : Less than
# >= : Greater than or equal to
# <= : Less than or equal to

print("Comparison Operators")
x = 5
y = 8
print("x == y:", x == y)     # False
print("x != y:", x != y)     # True
print("x > y:", x > y)        # False
print("x < y:", x < y)        # True
print("x >= y:", x >= y)      # False
print("x <= y:", x <= y)      # True
print()

# Assignment operators
# = : Assigns a value
# += : Adds and assigns
# -= : Subtracts and assigns
# *= : Multiplies and assigns
# /= : Divides and assigns
# %= : Modulus and assigns
# **= : Exponent and assigns

print("Assignment Operators")
num = 10
num += 5
print("num after += 5:", num)  # 15
num *= 2
print("num after *= 2:", num)  # 30
num /= 3
print("num after /= 3:", num)  # 10.0
print()

# Logical operators
# and : Returns True if both conditions are true
# or  : Returns True if at least one condition is true
# not : Reverses the result of a condition

print("Logical Operators")
flag1 = True
flag2 = False
print("flag1 and flag2:", flag1 and flag2)  # False
print("flag1 or flag2:", flag1 or flag2)    # True
print("not flag2:", not flag2)              # True
print()

# Bitwise operators
# & : Bitwise AND
# | : Bitwise OR
# ^ : Bitwise XOR
# ~ : Bitwise NOT
# << : Left shift
# >> : Right shift

print("Bitwise Operators")
left = 5      # 0101
right = 3     # 0011
print("left & right:", left & right)   # 1
print("left | right:", left | right)   # 7
print("left ^ right:", left ^ right)   # 6
print("~left:", ~left)                 # -6
print("left << 1:", left << 1)         # 10
print("left >> 1:", left >> 1)         # 2
print()

# Identity operators
# is  : Returns True if both variables refer to the same object
# is not : Returns True if both variables do not refer to the same object

print("Identity Operators")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 is list2:", list1 is list2)  # False
print("list1 is list3:", list1 is list3)  # True
print("list1 is not list2:", list1 is not list2)  # True
print()

# Membership operators
# in : Returns True if a value is found in a sequence
# not in : Returns True if a value is not found in a sequence

print("Membership Operators")
letters = ["a", "b", "c", "d"]
print("'b' in letters:", 'b' in letters)          # True
print("'x' not in letters:", 'x' not in letters)  # True
print()

# Ternary operator
# Syntax: value_if_true if condition else value_if_false

print("Ternary Operator")
age = 20
status = "Adult" if age >= 18 else "Minor"
print("status:", status)  # Adult
print()

# Summary of operator definitions
operator_definitions = {
    "Arithmetic": "Used for mathematical calculations like addition, subtraction, multiplication, division, and exponentiation.",
    "Comparison": "Used to compare two values and return True or False.",
    "Assignment": "Used to assign values to variables and update them.",
    "Logical": "Used to combine or invert boolean conditions.",
    "Bitwise": "Used to perform operations on binary digits (bits).",
    "Identity": "Used to check whether two variables refer to the same object in memory.",
    "Membership": "Used to check whether a value exists in a sequence such as a list, string, or tuple.",
    "Ternary": "A compact way to write a conditional expression."
}

print("Operator Definitions")
for name, definition in operator_definitions.items():
    print(f"{name}: {definition}")
