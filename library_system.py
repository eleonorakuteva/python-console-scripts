"""
Library Management System
Description: This program defines a Library system with Users and Librarians who can manage books.
==========================
-> Users can borrow and return books.
-> Librarians can add or remove books from a library.
-> Tracks total users and libraries.
-> Validates user library card numbers (must be 8 digits).
-> Prints current state of libraries and users.

"""

class Library:

    _total_libraries = 0

    def __init__(self, library_name:str, books = None):
        self.library_name = library_name
        self.books = books if books is not None else []
        Library._total_libraries += 1

    def __repr__(self):
        return (f"Library name: {self.library_name}\n"
                f"Library books: {self.books or 'None'}")

    def display_books(self):
        if not self.books:
            print(f"There are no books in the library {self.library_name}")
        elif len(self.books) > 1:
            print(f"There are {len(self.books)} books:\n"
                      f" -> {', '.join(self.books)}")
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

    def __repr__(self):
        return f"User: {self.full_name()} | Borrowed books: {self.borrowed_books or 'None'}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def borrow_book(self, book, library):
        if book in library.books:
            self.borrowed_books.append(book)
            library.books.remove(book)
            print(f"{self.full_name()} borrowed '{book}' from {library.library_name}.")
        else:
            print(f"'{book}' is not available in {library.library_name}.")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.books.append(book)
            print(f"{self.full_name()} returned '{book}' from {library.library_name}.")
        else:
            print(f"The book: '{book}' is not borrowed by {self.full_name()}.")


class Librarian(User):
    def __init__(self, first_name, last_name, librarian_id:str):
        super().__init__(first_name, last_name)
        self.librarian_id = librarian_id

    def add_book(self, book, library):
        if book not in library.books:
            print(f"{self.full_name()} added '{book} to {library.library_name}.")
            library.books.append(book)
        else:
            print(f"'{book}' already exist in {library.library_name}.")

    def remove_book(self, book, library):
        if book in library.books:
            print(f"{self.full_name()} removed '{book}' from {library.library_name}.")
            library.books.remove(book)
        else:
            print(f"The book: '{book}' not found in {library.library_name}.")



if __name__ == "__main__":

    # Create Libraries:
    library1 = Library("City Library", ["1984", "Python Basics", "The Hobbit"])
    library2 = Library("GreenLib")

    # Create Users:
    user1 = User("Eleonora", "Kuteva")
    user2 = User("Emma", "White")

    # User Interactions:
    user1.borrow_book("1984", library1)
    library1.display_books()

    user1.return_book("1984", library1)
    library1.display_books()

    # User Info:
    print(User.get_user_count())
    print(user1.full_name())
    print(user2.full_name())

    # Card Validation:
    print(user1.is_card_valid("12345678"))  # True

    # Librarian Actions:
    librarian1 = Librarian("Sonya", "White", "librarian_1")
    librarian1.add_book("To Kill a Mockingbird", library1)
    librarian1.remove_book("To Kill a Mockingbird", library1)

    # Print Final States:
    print(user1)
    print(library1)