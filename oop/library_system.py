# library_system.py

class Book:
    def __init__(self, title, author):
        """Base class constructor for a book."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a generic book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Constructor for an EBook, calls the base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation for EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Constructor for a PrintBook, calls the base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Constructor for Library, initializes an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Adds a book to the library collection."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """Prints details of all books in the library."""
        for book in self.books:
            print(book)
