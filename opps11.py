"""A small introduction to object-oriented programming in Python."""


class Person:
	"""Represent a person using attributes and methods."""

	species = "Human"  # Class attribute shared by every Person

	def __init__(self, name: str, age: int) -> None:
		self.name = name  # Instance attributes
		self.age = age

	def introduce(self) -> str:
		return f"Hi, I am {self.name} and I am {self.age} years old."

	def birthday(self) -> None:
		self.age += 1


class Student(Person):
	"""A Student inherits behavior from Person and adds a subject."""

	def __init__(self, name: str, age: int, subject: str) -> None:
		super().__init__(name, age)  # Call the parent constructor
		self.subject = subject

	def introduce(self) -> str:  # Method overriding (polymorphism)
		return f"{super().introduce()} I study {self.subject}."


if __name__ == "__main__":
	person = Person("Alex", 30)
	student = Student("Sam", 20, "Computer Science")

	print(person.introduce())
	print(student.introduce())

	student.birthday()
	print(f"{student.name} is now {student.age}.")
