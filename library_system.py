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
            print(f"There are {len(self.books)} books:\n"
                  f"{books_as_string}")


class LibraryUser:

    _user_count = 0

    @classmethod
    def get_user_count(cls):
        return LibraryUser._user_count

    def __init__(self, first_name:str, last_name:str, borrowed_books = None):
        self.first_name = first_name
        self.last_name = last_name
        self.borrowed_books = borrowed_books
        LibraryUser._user_count += 1

    @ property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def borrow_book(self, book, library):
        pass

    def return_book(self, library):
        pass

