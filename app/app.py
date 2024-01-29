from flask import Flask, request, jsonify
from data.books import books


app = Flask(__name__)

@app.route('/library/<book_id>', methods=['GET'])
def index(book_id):
    book = books[id == int(book_id)]

    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404
