# ============================================================================
# TASK 3: PYTHON CLASSES AND OBJECTS
# ============================================================================

# Topic 1: Class definition and object creation
print("--- Topic 1: Class definition and object creation ---")

class Dog:
    """A simple Dog class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", 3)
dog1.bark()
print(f"Dog's name: {dog1.name}, Age: {dog1.age}")

dog2 = Dog("Max", 5)
dog2.bark()




# Topic 2: The constructor method __init__()
print("\n--- Topic 2: The constructor method __init__() ---")

class Car:
    """A Car class with constructor"""
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.color} {self.brand}")

car1 = Car("Tesla", "red", 2023)
car1.display_info()

car2 = Car("BMW", "blue", 2022)
car2.display_info()




# Topic 3: Instance methods and the parameter self
print("\n--- Topic 3: Instance methods and the parameter self ---")

class Person:
    """Person class with instance methods"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        """Instance method using self"""
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")
    
    def have_birthday(self):
        """Instance method that modifies self"""
        self.age += 1
        print(f"{self.name} just turned {self.age}!")
    
    def is_adult(self):
        """Instance method returning boolean"""
        return self.age >= 18

person = Person("John", 30)
person.introduce()
person.have_birthday()
print(f"Is {person.name} an adult? {person.is_adult()}")




# Topic 4: Class variables vs instance variables
print("\n--- Topic 4: Class variables vs instance variables ---")

class Student:
    """Student class showing class vs instance variables"""
    total_students = 0  # Class variable (shared by all instances)
    
    def __init__(self, name, student_id):
        self.name = name  # Instance variable
        self.student_id = student_id  # Instance variable
        Student.total_students += 1
    
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.student_id}, Total students: {Student.total_students}")

student1 = Student("Alice", 101)
student1.display_info()

student2 = Student("Bob", 102)
student2.display_info()

student3 = Student("Charlie", 103)
student3.display_info()

print(f"Class variable - Total students: {Student.total_students}")




# Topic 5: Modifying and deleting object properties
print("\n--- Topic 5: Modifying and deleting object properties ---")

class Book:
    """Book class for modifying and deleting properties"""
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display(self):
        if hasattr(self, 'title'):
            print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")
        else:
            print("Title attribute has been deleted")

book = Book("Python 101", "John Doe", 350)
book.display()

# Modify properties
book.pages = 400
book.author = "Jane Doe"
book.display()

# Add new property
book.year_published = 2023
print(f"Year published: {book.year_published}")

# Delete property
del book.year_published
print(f"Has year_published attribute? {hasattr(book, 'year_published')}")




# Topic 6: Practical example - Bank Account
print("\n--- Topic 6: Practical example - Bank Account ---")

class BankAccount:
    """Bank Account class with multiple features"""
    interest_rate = 0.02  # Class variable
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Instance variable
        self.balance = balance  # Instance variable
    
    def deposit(self, amount):
        """Deposit money into account"""
        self.balance += amount
        print(f"{self.account_holder} deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")
    
    def apply_interest(self):
        """Apply interest to account"""
        self.balance += self.balance * self.interest_rate
        print(f"Interest applied. New balance: ${self.balance:.2f}")

account = BankAccount("Eve", 1000)
account.deposit(500)
account.withdraw(200)
account.apply_interest()
