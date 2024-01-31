from flask import Flask, request, jsonify
from data.books import books


app = Flask(__name__)

@app.route('/books', methods=['POST'])
def index():
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        author = request.form.get('author')
        publication_year = request.form.get('publication_year')
        genre = request.form.get('genre')

        # Filter books based on form data
        filtered_books = books
        if title:
            filtered_books = [book for book in filtered_books if book['title'] == title]
        if author:
            filtered_books = [book for book in filtered_books if book['author'] == author]
        if publication_year:
            filtered_books = [book for book in filtered_books if book['publication_year'] == int(publication_year)]
        if genre:
            filtered_books = [book for book in filtered_books if book['genre'] == genre]

        # Return the filtered books as JSON
        return jsonify(filtered_books)

if __name__ == '__main__':
    app.run(debug=True)