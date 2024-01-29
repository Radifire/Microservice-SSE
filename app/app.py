from flask import Flask, request, jsonify
from data.books import books


app = Flask(__name__)

@app.route('/books', methods=['GET'])
def bookList():
    return jsonify(books)


if __name__ == '__main__':
    app.run(debug=True)