

from functools import reduce


# 1. List comprehensions
# Definition: a concise way to create a list by transforming or selecting
# items from an iterable.
# Syntax: [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]
print("Squares:", squares)
print("Even numbers:", even_numbers)


# 2. map()
# Definition: applies a function to every item in an iterable and returns
# an iterator. Use it when each item needs the same transformation.

def cube(number):
    """Return the cube of a number."""
    return number ** 3


cubes = list(map(cube, numbers))
print("Cubes:", cubes)

# map() can also use a lambda for a short transformation.
upper_names = list(map(str.upper, ["adil ", "faruki", "ils"]))
print("Uppercase names:", upper_names)


# 3. filter()
# Definition: returns an iterator containing only items for which the
# predicate function returns True. Use it to select matching values.

def is_positive(number):
    """Return True when number is greater than zero."""
    return number > 0


values = [-3, 0, 4, -1, 7]
positive_values = list(filter(is_positive, values))
print("Positive values:", positive_values)


# 4. reduce()
# Definition: repeatedly combines items from an iterable into one value.
# Use it for cumulative operations such as a sum or product.

def multiply(left, right):
    """Return the product of two values."""
    return left * right


product = reduce(multiply, numbers)
print("Product:", product)

# Equivalent lambda examples:
total = reduce(lambda left, right: left + right, numbers, 0)
print("Total:", total)


# Quick comparison:
# - Comprehension: readable list creation and optional filtering.
# - map(): transform every item.
# - filter(): keep selected items.
# - reduce(): combine all items into one result.