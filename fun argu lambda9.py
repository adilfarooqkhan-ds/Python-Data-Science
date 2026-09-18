# Function definition:
# A function is a reusable block of code that performs a specific task.
# It is defined with `def`, followed by a name, parameters, and a body.
def greet(name):
    """Return a greeting for the supplied name."""
    return f"Hello, {name}!"


print(greet("Adil"))  # Call the function with an argument


# Arguments are values passed to a function's parameters.
def add_numbers(first, second=0):
    """Add two numbers; second has a default value."""
    return first + second


print(add_numbers(3, 4))          # positional arguments
print(add_numbers(first=5, second=2))  # keyword arguments
print(add_numbers(7))             # uses the default argument


# *args collects extra positional arguments in a tuple.
def total(*numbers):
    return sum(numbers)


# **kwargs collects extra keyword arguments in a dictionary.
def describe_person(**details):
    return details


print(total(1, 2, 3, 4))
print(describe_person(name="adil", age=24))


# Lambda function:
# A lambda is a small anonymous function written in one expression.
# Syntax: lambda parameters: expression
# It is useful for short, temporary operations, often with map, filter, or sort.
square = lambda number: number * number
print(square(6))

numbers = [1, 2, 3, 4, 5]
print(list(map(lambda number: number * 2, numbers)))
print(list(filter(lambda number: number % 2 == 0, numbers)))

students = [("adil", 82), ("ubaid", 95), ("ather", 88)]
students_by_score = sorted(students, key=lambda student: student[1], reverse=True)
print(students_by_score)