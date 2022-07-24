from flask import Flask, render_template

app = Flask(__name__)


def get_books():
    return [
        {
            "id": "12ew23e",
            "title": "Treasure Island",
            "author": "Robert Louis Stevenson",
            "year": 1993
        },
        {
            "id": "21df98i",
            "title": "Alice in Wonderland",
            "author": "Lewis Carroll",
            "year": 1995
        },
    ]


@app.route("/")
def index():
    return 'ok', 200


@app.route("/books")
def books():
    items = get_books()
    return render_template('books.html', books=items)


if __name__ == '__main__':
    app.run()
