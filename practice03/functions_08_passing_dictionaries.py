# ============================================================================
# TOPIC 8: Passing dictionaries as arguments
# ============================================================================

def display_student(student_dict):
    """Display student information from dictionary"""
    for key, value in student_dict.items():
        print(f"{key}: {value}")

student = {"name": "Frank", "age": 20, "grade": "A"}
display_student(student)









