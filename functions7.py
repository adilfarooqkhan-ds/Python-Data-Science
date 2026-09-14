def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def greet(name):
    """Return a greeting message for a given name."""
    return f"Hello, {name}! Welcome!"


def is_even(number):
    """Check whether a number is even."""
    return number % 2 == 0


def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


def factorial(n):
    """Return the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Example usage
if __name__ == "__main__":
    print("Addition example:", add_numbers(5, 7))
    print("Greeting example:", greet("Alice"))
    print("Even number example:", is_even(10))
    print("Area example:", calculate_area(4, 6))
    print("Factorial example:", factorial(5))
