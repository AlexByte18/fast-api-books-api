from classes.Book import Book
from constants import BOOKS


# class BookService:

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book
    