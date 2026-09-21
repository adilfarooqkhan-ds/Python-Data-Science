# 1. Inheritance: a child class reuses and extends a parent class.
class Animal:
    def speak(self):
        return "The animal makes a sound."


class Dog(Animal):
    def speak(self):
        return "The dog barks."


# 2. Polymorphism: the same method call can behave differently for each object.
class Cat(Animal):
    def speak(self):
        return "The cat meows."


# 3. Encapsulation: keep data private and access it through methods/properties.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Name-mangled private attribute

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


# 4. Destructor: __del__ is called when an object is being destroyed.
class TemporaryFile:
    def __init__(self, filename):
        self.filename = filename
        print(f"Opened {self.filename}")

    def __del__(self):
        print(f"Closing {self.filename}")


if __name__ == "__main__":
    # Inheritance
    dog = Dog()
    print(dog.speak())

    # Polymorphism
    for animal in (Dog(), Cat()):
        print(animal.speak())

    # Encapsulation
    account = BankAccount(100)
    account.deposit(50)
    print("Balance:", account.balance)

    # Destructor (timing depends on Python's garbage collector)
    temporary_file = TemporaryFile("example.txt")
    del temporary_file