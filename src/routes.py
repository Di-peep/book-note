from datetime import datetime

from flask import request
from flask_restful import Resource

from src import api, db
from src.models import Book


class Smoke(Resource):
    def get(self):
        return {'message': 'ok'}, 200


class Books(Resource):
    def get(self, uuid=None):
        if not uuid:
            books = db.session.query(Book).all()
            books = [book.to_dict() for book in books]
            return books, 200

        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if book:
            return book.to_dict(), 200

        return {'message': 'not found'}, 404

    def post(self):
        book = request.json
        if not book:
            return {'message': 'wrong data'}, 400

        try:
            book = Book(
                title=book["title"],
                author=book["author"],
                description=book["description"],
                release_date=datetime.strptime(book["release_date"], "%Y %m %d"),
                publisher=book.get("publisher"),
                language=book.get("language", "eng"),
                rating=book.get("rating", 0.0)
            )
            db.session.add(book)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'wrong data'}, 400

        return {'message': 'Created resource'}, 201

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self, uuid):
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return {'message': 'wrong data'}, 400

        db.session.delete(book)
        db.session.commit()
        return {'message': 'Resource was deleted'}, 204


api.add_resource(Smoke, '/smoke', '/smoke/', strict_slashes=False)
api.add_resource(Books, '/books', '/books/<uuid>', strict_slashes=False)
