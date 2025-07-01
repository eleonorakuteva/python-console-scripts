class Library:
    _total_libraries = 0
    def __init__(self, library_name:str, books = None):
        self.library_name = library_name
        self.books = books if books is not None else []
        Library._total_libraries += 1

    def display_books(self):
        if not self.books:
            print(f"There are no books in the library {self.library_name}")
        elif len(self.books) > 1:
            print(f"There are {len(self.books)} books:\n"
                      f" -> {", ".join(self.books)}")
        elif len(self.books) == 1:
            print(f"There is only one book left:\n"
                  f" -> {self.books[0]}")



class User:

    _user_count = 0

    @classmethod
    def get_user_count(cls):
        return User._user_count

    # Card number must be exactly 8 digits
    @staticmethod
    def is_card_valid(card:str):
        return len(card) == 8 and card.isdigit()

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
            print(f"{self.full_name()} borrowed '{book}' from {library.library_name}.")
        else:
            print(f"'{book}' is not available in {library.library_name}")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.books.append(book)
            print(f"{self.full_name()} returned '{book} from {library.library_name}.")
        else:
            print(f"The book: '{book}' is not borrowed by {self.full_name()}")


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
print(user1.is_card_valid("12345678"))  # True/False
