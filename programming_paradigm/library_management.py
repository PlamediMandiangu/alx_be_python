class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, the book is available
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"Checked out: {self.title}")
        else:
            print(f"Sorry, '{self.title}' is already checked out.")
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"Returned: {self.title}")
        else:
            print(f"'{self.title}' wasn't checked out.")
    
    def is_checked_out(self):
        return self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list of books
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return
        print(f"'{title}' is either not in the library or already checked out.")
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return
        print(f"'{title}' is not checked out or not in the library.")
    
    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books.")
