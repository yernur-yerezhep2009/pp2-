# ============================================================================
# TOPIC 9: Function documentation with docstrings
# ============================================================================

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









