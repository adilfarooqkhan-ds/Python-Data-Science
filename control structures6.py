# Control Structures in Python
# Control structures are statements that control the flow of execution in a program.
# They allow the program to make decisions, repeat tasks, and skip or stop execution based on conditions.

# 1. If statement
# Definition: Executes a block of code only if a condition is true.

a = 10
if a > 5:
    print("a is greater than 5")

# Example:
age = 18
if age >= 18:
    print("You are eligible to vote.")

# 2. If-Else statement
# Definition: Executes one block if the condition is true, otherwise another block.

number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. If-Elif-Else statement
# Definition: Checks multiple conditions in sequence.

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# 4. For loop
# Definition: Repeats a block of code for each item in a sequence.

for i in range(1, 6):
    print("Iteration:", i)

# Example with a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# 5. While loop
# Definition: Repeats a block of code as long as a condition remains true.

count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# 6. Break statement
# Definition: Stops the loop immediately when a condition is met.

for num in range(1, 10):
    if num == 5:
        break
    print(num)

# 7. Continue statement
# Definition: Skips the current iteration and moves to the next one.

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# 8. Nested control structures
# Definition: Using one control structure inside another.

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Summary
# Control structures help us control how a program runs based on conditions and repetitions.
# They are essential for decision-making and automating repeated tasks in Python.
