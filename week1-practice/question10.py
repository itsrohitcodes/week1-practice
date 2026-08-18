class LibraryBook:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return "Book borrowed successfully."

        return "Book is already borrowed."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return "Book returned successfully."

        return "Book is already available."

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"

        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Price: ₹{self.price}\n"
            f"Status: {status}"
        )


class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        for book in self.books:
            print(book)
            print()

    def search_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book

        return None

    def count_books(self):
        available = 0
        borrowed = 0

        for book in self.books:
            if book.is_available:
                available += 1
            else:
                borrowed += 1

        return available, borrowed


# Create books
book1 = LibraryBook("Python", "Rohit", 500)
book2 = LibraryBook("Java", "Salman", 600)
book3 = LibraryBook("SQL", "Vinay", 400)

# Create library
library = LibraryManager()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


# Display books
print("All Books:")
library.display_books()


# Search for a book
title = input("Enter book title: ").strip()
book = library.search_by_title(title)

if book:
    print("\nBook Found:")
    print(book)

    choice = input("\nDo you want to borrow this book? ").strip().lower()

    if choice == "yes":
        print(book.borrow_book())
        print()
        print(book)
else:
    print("Book not found.")


# Display library statistics
available, borrowed = library.count_books()

print("\nLibrary Statistics:")
print("Available Books:", available)
print("Borrowed Books:", borrowed)