import uuid

from src import db


class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    title = db.Column(db.String(120), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)
    author = db.relationship("Author", back_populates="books")

    description = db.Column(db.Text, unique=True, nullable=False)
    release_date = db.Column(db.Date)
    publisher = db.Column(db.String(60))
    language = db.Column(db.String(20))
    rating = db.Column(db.Float)

    def __init__(self, title, author, description, release_date, publisher, language, rating):
        self.uuid = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.description = description
        self.release_date = release_date
        self.publisher = publisher
        self.language = language
        self.rating = rating

    def __repr__(self):
        return f'Book({self.uuid}, {self.title}, {self.author})'


class Author(db.Model):
    __tablename__ = "author"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    books = db.relationship("Book", back_populates="author")

    def __init__(self, name, description="", books=None):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.description = description
        if not books:
            self.books = []
        else:
            self.books = books

    def __repr__(self):
        return f"Author({self.uuid}, {self.name})"
