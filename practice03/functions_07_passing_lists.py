# ============================================================================
# TOPIC 7: Passing lists as arguments
# ============================================================================

def process_list(items):
    """Process a list of items"""
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

numbers = [10, 20, 30, 40]
process_list(numbers)

print()

fruits = ["Apple", "Banana", "Cherry"]
process_list(fruits)









