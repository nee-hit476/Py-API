# controllers/book_controller.py

from flask import jsonify, request
from models.book import Book

def get_books():
    return jsonify(Book.get_all()), 200

def get_book(book_id):
    book = Book.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200

def add_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    new_book = Book.create(data['title'], data['author'])
    return jsonify(new_book), 201

def update_book(book_id):
    data = request.get_json()
    book = Book.update(book_id, data.get("title"), data.get("author"))
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200

def delete_book(book_id):
    book = Book.delete(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({"message": "Book deleted", "book": book}), 200
