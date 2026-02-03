# ============================================================================
# TOPIC 6: Function with return values
# ============================================================================

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









