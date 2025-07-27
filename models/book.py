# models/book.py

class Book:
    books = {
        1: {"id": 1, "title": "1984", "author": "George Orwell"},
        2: {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    }
    next_id = 3

    @classmethod
    def get_all(cls):
        return list(cls.books.values())

    @classmethod
    def get(cls, book_id):
        return cls.books.get(book_id)

    @classmethod
    def create(cls, title, author):
        new_book = {"id": cls.next_id, "title": title, "author": author}
        cls.books[cls.next_id] = new_book
        cls.next_id += 1
        return new_book

    @classmethod
    def update(cls, book_id, title=None, author=None):
        if book_id not in cls.books:
            return None
        if title:
            cls.books[book_id]["title"] = title
        if author:
            cls.books[book_id]["author"] = author
        return cls.books[book_id]

    @classmethod
    def delete(cls, book_id):
        return cls.books.pop(book_id, None)
