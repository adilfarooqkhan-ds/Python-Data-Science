"""Classes, objects, constructors, and destructors in Python.

Class       : A blueprint that defines data and behavior for objects.
Object      : An instance created from a class.
Constructor : The __init__ method, called automatically when an object is created, usually to initialize its attributes.
Destructor  : The __del__ method, called when an object is being removed by Python's garbage collector.
"""


class Student:
    """Example class representing a student."""

    school = "Python Academy"  # Class attribute shared by all students

    def __init__(self, name, age):
        """Constructor: initialize each new Student object."""
        self.name = name
        self.age = age
        print(f"Constructor called for {self.name}")

    def introduce(self):
        """Display information about this object."""
        print(f"Name: {self.name}, Age: {self.age}, School: {self.school}")

    def __del__(self):
        """Destructor: called when this object is about to be destroyed."""
        print(f"Destructor called for {self.name}")


if __name__ == "__main__":
    # student1 and student2 are objects (instances) of Student.
    student1 = Student("Asha", 20)
    student2 = Student("Ravi", 21)

    student1.introduce()
    student2.introduce()

    # __del__ may be called here; exact timing depends on Python's implementation.
    del student1
    del student2