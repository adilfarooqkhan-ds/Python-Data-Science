"""Exception handling lets a program respond to runtime errors. Debugging is the
process of finding and correcting errors in a program.
"""


# try wraps code that may fail; except handles a specific exception.
def divide(a, b):
	try:
		return a / b
	except ZeroDivisionError:
		print("Cannot divide by zero.")
		return None


# else runs only when try succeeds. finally runs whether it succeeds or fails.
def parse_integer(text):
	try:
		value = int(text)
	except ValueError as error:
		print(f"Invalid integer: {error}")
		return None
	else:
		print("Conversion succeeded.")
		return value
	finally:
		print("Conversion attempt finished.")


# raise is used to report invalid input explicitly.
def validate_age(age):
	if age < 0:
		raise ValueError("Age cannot be negative.")
	return age


# Debugging: inspect intermediate values; use breakpoint() to pause execution
# and step through the function with Python's interactive debugger.
def average(values):
	assert values, "values must not be empty"
	total = sum(values)
	count = len(values)
	result = total / count
	print(f"DEBUG: total={total}, count={count}, average={result}")
	return result


if __name__ == "__main__":
	print("10 / 2:", divide(10, 2))
	print("10 / 0:", divide(10, 0))
	print("Parsed:", parse_integer("42"))
	print("Parsed:", parse_integer("hello"))
	try:
		validate_age(-1)
	except ValueError as error:
		print("Handled invalid age:", error)
	print("Average:", average([2, 4, 6]))
