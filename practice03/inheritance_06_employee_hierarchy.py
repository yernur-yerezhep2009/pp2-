# ============================================================================
# TOPIC 6: Practical example - Employee hierarchy
# ============================================================================

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









