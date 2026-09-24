"""Magic methods and operator overloading."""


class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f"Vector({self.x}, {self.y})"

	def __str__(self):
		return f"({self.x}, {self.y})"

	def __add__(self, other):
		if not isinstance(other, Vector):
			return NotImplemented
		return Vector(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		if not isinstance(other, Vector):
			return NotImplemented
		return Vector(self.x - other.x, self.y - other.y)

	def __mul__(self, number):
		if not isinstance(number, (int, float)):
			return NotImplemented
		return Vector(self.x * number, self.y * number)

	def __rmul__(self, number):
		return self * number

	def __eq__(self, other):
		return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)

	def __len__(self):
		return 2

	def __getitem__(self, index):
		return (self.x, self.y)[index]


if __name__ == "__main__":
	first = Vector(2, 3)
	second = Vector(4, 1)

	print(first + second)  # __add__
	print(first - second)  # __sub__
	print(first * 2)       # __mul__
	print(2 * first)       # __rmul__
	print(first == Vector(2, 3))  # __eq__
	print(len(first), first[0])    # __len__, __getitem__
