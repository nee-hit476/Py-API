# app.py

from flask import Flask
from routes.book_routes import book_bp

app = Flask(__name__)
app.register_blueprint(book_bp, url_prefix="/books")

if __name__ == '__main__':
    app.run(debug=True)
