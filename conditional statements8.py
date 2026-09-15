# if statement: executes code when a condition is True.
age = 20
if age >= 18:
	print("Adult")

# if-else statement: chooses between two blocks of code.
number = 7
if number % 2 == 0:
	print("Even")
else:
	print("Odd")

# if-elif-else statement: checks several conditions in order.
score = 82
if score >= 90:
	grade = "A"
elif score >= 75:
	grade = "B"
else:
	grade = "C"
print("Grade:", grade)

# for loop: repeats code for each item in a sequence or range.
for fruit in ["apple", "banana", "mango"]:
	print(fruit)

# while loop: repeats code while a condition is True.
count = 1
while count <= 3:
	print("Count:", count)
	count += 1

# def: defines a reusable function that performs a task.
def show_even_numbers(limit):
	"""Print even numbers from 1 through limit."""
	for value in range(1, limit + 1):
		if value % 2 == 0:
			print(value)


show_even_numbers(10)
