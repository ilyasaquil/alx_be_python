# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Print a message when the book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Informal string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# For direct testing without needing main.py
if __name__ == "__main__":
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrate __str__
    print(my_book)

    # Demonstrate __repr__
    print(repr(my_book))

    # Trigger __del__
    del my_book
