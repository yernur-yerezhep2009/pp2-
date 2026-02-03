# ============================================================================
# TASK 2: PYTHON LAMBDA EXPRESSIONS
# ============================================================================

# Topic 1: Lambda syntax and basic usage
print("--- Topic 1: Lambda syntax and basic usage ---")

# Simple lambda function to square a number
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")
print(f"Square of 10: {square(10)}")

# Lambda with multiple arguments
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")




# Topic 2: Using lambda with map() for transformation
print("\n--- Topic 2: Using lambda with map() ---")

# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Square each number in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")




# Topic 3: Using lambda with filter() for selection
print("\n--- Topic 3: Using lambda with filter() ---")

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"All numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Numbers greater than 5: {greater_than_5}")




# Topic 4: Using lambda with sorted() for custom sorting
print("\n--- Topic 4: Using lambda with sorted() ---")

# Sort students by score (descending)
students = [("Alice", 85), ("Bob", 75), ("Charlie", 90), ("Diana", 88)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by score (descending): {sorted_by_score}")

# Sort by name length
words = ["python", "java", "c", "javascript", "go"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"Words sorted by length: {sorted_by_length}")




# Topic 5: Anonymous functions vs regular functions
print("\n--- Topic 5: Anonymous functions vs regular functions ---")

# Using regular function
def multiply(a, b):
    """Regular function to multiply two numbers"""
    return a * b

# Using lambda (anonymous function)
multiply_lambda = lambda a, b: a * b

print(f"Regular function: 4 * 5 = {multiply(4, 5)}")
print(f"Lambda function: 4 * 5 = {multiply_lambda(4, 5)}")

# Lambda in action with map
numbers = [1, 2, 3, 4, 5]
result_regular = list(map(multiply, numbers, [2, 2, 2, 2, 2]))
result_lambda = list(map(lambda x: x * 2, numbers))
print(f"Map with regular function: {result_regular}")
print(f"Map with lambda function: {result_lambda}")




# Topic 6: Combining lambda with other functions
print("\n--- Topic 6: Combining lambda with multiple functions ---")

# Complex filtering and mapping
data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 20}]
names_of_adults = list(map(lambda x: x["name"].upper(), filter(lambda x: x["age"] >= 25, data)))
print(f"Adults (age >= 25) in uppercase: {names_of_adults}")

# Nested sorting and filtering
products = [("Laptop", 999), ("Mouse", 25), ("Keyboard", 75), ("Monitor", 300)]
expensive = sorted(filter(lambda x: x[1] > 50, products), key=lambda x: x[1], reverse=True)
print(f"Expensive products (>50) sorted by price: {expensive}")
