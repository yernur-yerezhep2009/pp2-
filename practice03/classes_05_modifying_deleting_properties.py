# ============================================================================
# TOPIC 5: Modifying and deleting object properties
# ============================================================================

class Book:
    """Book class for modifying and deleting properties"""
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display(self):
        if hasattr(self, 'title'):
            print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")
        else:
            print("Title attribute has been deleted")

book = Book("Python 101", "John Doe", 350)
book.display()

# Modify properties
book.pages = 400
book.author = "Jane Doe"
book.display()

# Add new property
book.year_published = 2023
print(f"Year published: {book.year_published}")

# Delete property
del book.year_published
print(f"Has year_published attribute? {hasattr(book, 'year_published')}")









