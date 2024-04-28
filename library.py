class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books in the library:")
            for book in self.books:
                if book.available:
                    print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"You have borrowed '{book.title}'. Enjoy reading!")
                else:
                    print(f"'{book.title}' is not available for borrowing.")
                return
        print(f"Sorry, '{title}' is not available in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"Thank you for returning '{book.title}'.")
                else:
                    print(f"'{book.title}' is already available in the library.")
                return
        print(f"Sorry, '{title}' is not a valid book to return.")


# Example usage
if __name__ == "__main__":
    library = Library()

    book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.display_books()

    library.borrow_book("Harry Potter and the Philosopher's Stone")
    library.borrow_book("To Kill a Mockingbird")
    library.borrow_book("The Great Gatsby")
    library.borrow_book("The Catcher in the Rye")

    library.return_book("To Kill a Mockingbird")
    library.return_book("To Kill a Mockingbird")

    library.display_books()
