# ============================================================================
# TASK 1: PYTHON FUNCTIONS
# ============================================================================

# Topic 1: Function definition and calling
print("--- Topic 1: Function definition and calling ---")

def my_function():
    """A simple function that prints a greeting"""
    print("Hello from a function")

my_function()
my_function()




# Topic 2: Function with positional arguments
print("\n--- Topic 2: Function with positional arguments ---")

def greet(name, age):
    """Greet a person with their name and age"""
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 25)
greet("Bob", 30)




# Topic 3: Function with default arguments
print("\n--- Topic 3: Function with default arguments ---")

def welcome(name="Guest", status="user"):
    """Welcome a person with default values"""
    print(f"Welcome, {name}! Status: {status}")

welcome()
welcome("Charlie")
welcome("Diana", "admin")




# Topic 4: Function with *args (variable positional arguments)
print("\n--- Topic 4: Function with *args ---")

def sum_all(*args):
    """Sum all provided arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")




# Topic 5: Function with **kwargs (keyword arguments)
print("\n--- Topic 5: Function with **kwargs ---")

def print_info(**kwargs):
    """Print key-value pairs"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Eve", age=28, city="New York")
print_info(product="Laptop", price=999, brand="Dell")




# Topic 6: Function with return values
print("\n--- Topic 6: Function with return values ---")

def calculate(a, b, operation):
    """Perform calculation based on operation"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Error: Division by zero"

result1 = calculate(10, 5, "add")
result2 = calculate(10, 5, "subtract")
print(f"10 + 5 = {result1}")
print(f"10 - 5 = {result2}")




# Topic 7: Passing lists as arguments
print("\n--- Topic 7: Passing lists as arguments ---")

def process_list(items):
    """Process a list of items"""
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

numbers = [10, 20, 30, 40]
process_list(numbers)

fruits = ["Apple", "Banana", "Cherry"]
process_list(fruits)




# Topic 8: Passing dictionaries as arguments
print("\n--- Topic 8: Passing dictionaries as arguments ---")

def display_student(student_dict):
    """Display student information from dictionary"""
    for key, value in student_dict.items():
        print(f"{key}: {value}")

student = {"name": "Frank", "age": 20, "grade": "A"}
display_student(student)




# Topic 9: Function documentation with docstrings
print("\n--- Topic 9: Function documentation with docstrings ---")

def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle
    
    Returns:
        The area of the circle
    
    Example:
        >>> calculate_area(5)
        78.5
    """
    import math
    return math.pi * radius ** 2

area = calculate_area(5)
print(f"Area of circle with radius 5: {area:.2f}")
print(f"Function docstring: {calculate_area.__doc__}")




# Topic 10: Multiple return values
print("\n--- Topic 10: Multiple return values ---")

def get_min_max(numbers):
    """Return minimum and maximum values from a list"""
    return min(numbers), max(numbers)

values = [15, 3, 42, 8, 99, 5]
min_val, max_val = get_min_max(values)
print(f"Min: {min_val}, Max: {max_val}")
