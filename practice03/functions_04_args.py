# ============================================================================
# TOPIC 4: Function with *args (variable positional arguments)
# ============================================================================

def sum_all(*args):
    """Sum all provided arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")









