# ============================================================================
# TOPIC 5: Anonymous functions vs regular functions
# ============================================================================

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









