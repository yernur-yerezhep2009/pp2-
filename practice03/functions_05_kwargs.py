# ============================================================================
# TOPIC 5: Function with **kwargs (keyword arguments)
# ============================================================================

def print_info(**kwargs):
    """Print key-value pairs"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Eve", age=28, city="New York")
print_info(product="Laptop", price=999, brand="Dell")









