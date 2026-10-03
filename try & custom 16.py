class InvalidAgeError(ValueError):
	"""Raised when an age is outside the accepted range."""


def describe_age(value):
	try:
		age = int(value)
	except (TypeError, ValueError) as error:
		raise InvalidAgeError("Age must be a whole number.") from error

	if not 0 <= age <= 120:
		raise InvalidAgeError("Age must be between 0 and 120.")
	return f"Age: {age}"


if __name__ == "__main__":
	for value in ("25", "not a number", "150"):
		try:
			print(describe_age(value))
		except InvalidAgeError as error:
			print(f"Invalid input: {error}")
		else:
			print("Input accepted.")
		finally:
			print("Validation finished.\n")
