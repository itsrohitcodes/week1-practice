# question 10

# class book
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
        self.is_available = True
        return "Book returned successfully."

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} | {self.author} | {self.price} | {status}"

# library class
class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def search_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book


# Books
book1 = LibraryBook("Python", "Rohit", 500)
book2 = LibraryBook("Java", "Salman", 600)
book3 = LibraryBook("SQL", "Vinay", 400)

# Library
library = LibraryManager()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display books
library.display_books()

# Search
title = input()
book = library.search_by_title(title)

if book:
    print(f"Book found: {book}")

    choice = input()

    if choice.lower() == "yes":
        print(book.borrow_book())
        print(book)
else:
    print("Book not found.")

# Count books
available = 0
borrowed = 0

for book in library.books:
    if book.is_available:
        available += 1
    else:
        borrowed += 1

# Print the results
print("Available books:", available)
print("Borrowed books:", borrowed)