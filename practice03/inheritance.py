# ============================================================================
# TASK 4: PYTHON INHERITANCE
# ============================================================================

# Topic 1: Parent and child class relationships
print("--- Topic 1: Parent and child class relationships ---")

class Animal:
    """Parent class - Animal"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    """Child class - Dog inherits from Animal"""
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    """Child class - Cat inherits from Animal"""
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
dog.speak()

cat = Cat("Whiskers")
cat.speak()




# Topic 2: Using super() to call parent methods
print("\n--- Topic 2: Using super() to call parent methods ---")

class Vehicle:
    """Parent class - Vehicle"""
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def display(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

class Car(Vehicle):
    """Child class - Car inherits from Vehicle"""
    def __init__(self, brand, color, car_type):
        super().__init__(brand, color)  # Call parent constructor
        self.car_type = car_type
    
    def display(self):
        super().display()  # Call parent method
        print(f"Type: {self.car_type}")

car = Car("Toyota", "blue", "Sedan")
car.display()




# Topic 3: Method overriding
print("\n--- Topic 3: Method overriding ---")

class Shape:
    """Parent class - Shape"""
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """This method will be overridden in child classes"""
        pass

class Rectangle(Shape):
    """Child class - Rectangle overrides area method"""
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    
    def area(self):
        """Overridden method"""
        return self.width * self.height

class Circle(Shape):
    """Child class - Circle overrides area method"""
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        """Overridden method"""
        import math
        return math.pi * self.radius ** 2

rectangle = Rectangle("Rectangle", 5, 10)
print(f"{rectangle.name} area: {rectangle.area()}")

circle = Circle("Circle", 5)
print(f"{circle.name} area: {circle.area():.2f}")




# Topic 4: Multiple inheritance
print("\n--- Topic 4: Multiple inheritance ---")

class Flyer:
    """Mixin class - Flyer"""
    def fly(self):
        print("Flying...")

class Swimmer:
    """Mixin class - Swimmer"""
    def swim(self):
        print("Swimming...")

class Diver:
    """Mixin class - Diver"""
    def dive(self):
        print("Diving...")

class Duck(Flyer, Swimmer):
    """Child class inheriting from Flyer and Swimmer"""
    def quack(self):
        print("Quack!")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()

print()

class Penguin(Swimmer, Diver):
    """Child class inheriting from Swimmer and Diver"""
    def waddle(self):
        print("Waddling...")

penguin = Penguin()
penguin.swim()
penguin.dive()
penguin.waddle()




# Topic 5: Inheritance chain and method resolution order (MRO)
print("\n--- Topic 5: Inheritance chain and MRO ---")

class A:
    def method(self):
        print("Method from class A")

class B(A):
    def method(self):
        print("Method from class B")

class C(A):
    def method(self):
        print("Method from class A")

class D(B, C):
    pass

d = D()
d.method()  # Shows MRO - B is checked before C

print(f"MRO for class D: {[cls.__name__ for cls in D.__mro__]}")




# Topic 6: Practical example - Employee hierarchy
print("\n--- Topic 6: Practical example - Employee hierarchy ---")

class Employee:
    """Parent class - Employee"""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")
    
    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name}'s salary increased by ${amount}")

class Manager(Employee):
    """Child class - Manager"""
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Developer(Employee):
    """Child class - Developer"""
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

manager = Manager("Frank", 80000, "Engineering")
manager.display_info()
manager.give_raise(5000)

print()

developer = Developer("Grace", 70000, "Python")
developer.display_info()
developer.give_raise(3000)
