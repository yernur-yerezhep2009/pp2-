# ============================================================================
# TOPIC 6: Combining lambda with other functions
# ============================================================================

# Complex filtering and mapping
data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 20}]
names_of_adults = list(map(lambda x: x["name"].upper(), filter(lambda x: x["age"] >= 25, data)))
print(f"Adults (age >= 25) in uppercase: {names_of_adults}")

# Nested sorting and filtering
products = [("Laptop", 999), ("Mouse", 25), ("Keyboard", 75), ("Monitor", 300)]
expensive = sorted(filter(lambda x: x[1] > 50, products), key=lambda x: x[1], reverse=True)
print(f"Expensive products (>50) sorted by price: {expensive}")









