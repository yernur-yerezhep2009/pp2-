# ============================================================================
# TOPIC 10: Multiple return values
# ============================================================================

def get_min_max(numbers):
    """Return minimum and maximum values from a list"""
    return min(numbers), max(numbers)

values = [15, 3, 42, 8, 99, 5]
min_val, max_val = get_min_max(values)
print(f"Min: {min_val}, Max: {max_val}")









