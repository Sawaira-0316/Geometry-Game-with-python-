# class animaml:
#     def __init__(self,name,gender):
#           self.name=name
#           self.gender=gender
#
# class Brids(animaml):
#     def __init__(self ,name,gender,flying):
#         super().__init__(name,gender)
#         self.flying=flying
#     def decribe(self):
#         print("Parraot is flying animal")
#
# obj=Brids("Parrorts","Female","flying")
# #print("name:",obj.name)
# ##print("Gender:",obj.gender)
# #obj.decribe()
#
#              ##### Practice OOP Project
# Create a simple library management system in Python using OOP principles. The system should allow users to manage
# books, authors, and library patrons. It should providefunctionality to borrow and return books, as well as maintain
# records of available books and overdue book
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

class Book:
    def __init__(self, title, isbn, author):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.available = True

class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.authors = []
        self.patrons = []

    def add_author(self, author):
        self.authors.append(author)

    def add_book(self, book):
        self.books.append(book)
        book.author.books.append(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            book.author.books.remove(book)

    def borrow_book(self, patron, book):
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
        else:
            print("Book is not available for borrowing.")

    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)
        else:
            print("This book was not borrowed by the patron.")

    def display_books(self):
        for book in self.books:
            if book.available:
                print(f"Title: {book.title}, Author: {book.author.name}")

    def display_overdue_books(self):
        # Implement logic to display overdue books if needed
        pass

if __name__ == "__main__":
    author1 = Author("Sawaira Asghar")
    author2 = Author("Jhon")
    book1 = Book("Python Basics", "1010", author1)
    book2 = Book("Data Science", "1011", author2)
    patron1 = Patron("sajida")
    library = Library()

    library.add_author(author1)
    library.add_author(author2)
    library.add_book(book1)
    library.add_book(book2)
    library.add_patron(patron1)

    print("Available Books:")
    library.display_books()
    library.borrow_book(patron1, book1)

    print(f"\nBooks Borrowed by {patron1.name}:")
    for book in patron1.borrowed_books:
        print(f"Title: {book.title}, Author: {book.author.name}")

    library.return_book(patron1, book1)

    print("\nAvailable Books:")
    library.display_books()
