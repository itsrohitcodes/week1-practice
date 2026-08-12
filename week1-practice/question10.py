# Library Book Manager

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
        else:
            return "Book is already borrowed."

    def return_book(self):
        self.is_available = True
        return "Book returned successfully."

    def __str__(self):
        if self.is_available:
            status = "Available"
        else:
            status = "Borrowed"

        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Price: {self.price}\n"
            f"Status: {status}"
        )

class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)
            print()

    def search_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

# Create books
book1 = LibraryBook("Python", "Rohit", 500)
book2 = LibraryBook("Java", "Salman", 600)
book3 = LibraryBook("SQL", "Vinay", 400)

library = LibraryManager()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("All Books:")
library.display_books()
title = input()
book = library.search_by_title(title)

if book:
    print(book)
    choice = input("Do you want to borrow this book? ")
    if choice.lower() == "yes":
        print(book.borrow_book())
        print(book)
else:
    print("Book not found.")

available = 0
borrowed = 0

for book in library.books:
    if book.is_available:
        available += 1
    else:
        borrowed += 1

print("Available Books:", available)
print("Borrowed Books:", borrowed)