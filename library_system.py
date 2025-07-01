class Library:
    _total_libraries = 0
    def __init__(self, library_name:str, books = None):
        self.library_name = library_name
        self.books = books
        Library._total_libraries += 1

    def display_books(self):
        if self.books is None:
            print(f"There are no books in the library {self.library_name}")
        else:
            books_as_string = ", ".join(self.books)
            if len(self.books) > 1:
                print(f"There are {len(self.books)} books:\n"
                      f"{books_as_string}")
            if len(self.books) == 1:
                print(f"There is only one book left:\n"
                      f"{books_as_string}")



class User:

    _user_count = 0

    @classmethod
    def get_user_count(cls):
        return User._user_count

    def __init__(self, first_name:str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name
        self.borrowed_books = []
        User._user_count += 1

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def borrow_book(self, book, library):
        if book in library.books:
            self.borrowed_books.append(book)
            library.books.remove(book)

    def return_book(self, book, library):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.books.append(book)


library1 = Library("City Library", ["1984", "Python Basics", "The Hobbit"])

user1 = User("Anna", "Ivanova")
print(user1.full_name())  # Anna Ivanova

user1.borrow_book("1984", library1)
library1.display_books()  # Should no longer include "1984"

user1.return_book("1984", library1)
library1.display_books()  # "1984" is back
#
print(User.get_user_count())  # e.g., 1
user2 = User("Emma", "White")
user2.first_name = "Comma"
print(user2.full_name())
print(User.get_user_count())


user1.borrow_book("1984", library1)
user2.borrow_book("Python Basics", library1)
library1.display_books()  # Only one book


#
# print(User.is_valid_card("12345678"))  # True
# print(User.is_valid_card("abc"))       # False