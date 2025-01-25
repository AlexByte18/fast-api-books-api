from typing import Optional
from fastapi import FastAPI, HTTPException, Path, Query

from classes.Book import Book
from constants import BOOKS
from schemas.BookRequest import BookRequest
from services.BookService import find_book_id

app = FastAPI()

@app.get("/books")
async def get_books(published_year: Optional[int] = Query(gt=0, lt=2025)):
    return BOOKS

@app.get("/books/{book_id}")
async def get_book(book_id: int = Path(gt=0)):
    print(">>>get_book")
    for book in BOOKS: 
        if book.id == book_id:
            print(">>>book found", book)
            BOOKS.remove(book)
            return book
        
    raise HTTPException(status_code=404, detail='Book not found')

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    try: 
        print(type(book_request))
        book_data = book_request.model_dump()
        new_book = Book(**book_data)
        BOOKS.append(find_book_id(new_book))
    except TypeError as e:
        print(f"Error: {e}")  # Imprime el error detallado
        return {"error": f"Type error occurred: {e}"}
    except Exception as e:
        print(f"Unexpected error: {e}")  # Captura errores generales
        return {"error": f"An unexpected error occurred: {e}"}

@app.put("/books/update_book")
async def update_book(book: BookRequest):
    updated_book = Book(**book.model_dump())

    for i in range(len(BOOKS)): 
        if BOOKS[i].id == updated_book.id:
            BOOKS[i] = updated_book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    print(">>>delete_book")
    for book in BOOKS: 
        if book.id == book_id:
            print(">>>book_to_delte", book)
            BOOKS.remove(book)
            break