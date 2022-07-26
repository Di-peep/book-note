import uuid

from src import db


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    uid = uuid.uuid4()
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)
    release_date = db.Column(db.Date)
    publisher = db.Column(db.String(60))
    language = db.Column(db.String(20))
    rating = db.Column(db.Float)

    def __init__(self, uid, title, author, description, release_date, publisher, language, rating):
        self.uid = uid
        self.title = title
        self.author = author
        self.description = description
        self.release_date = release_date
        self.publisher = publisher
        self.language = language
        self.rating = rating

    def __repr__(self):
        return f'Book({self.uid}, {self.title}, {self.author})'

    def to_dict(self):
        return {
            "uid": self.uid,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "release_date": self.release_date,
            "publisher": self.publisher,
            "language": self.language,
            "rating": self.rating
        }
