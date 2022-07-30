from datetime import datetime

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import api, db
from src.models import Book
from src.schemas import BookSchema


class Smoke(Resource):
    def get(self):
        return {'message': 'ok'}, 200


class Books(Resource):
    book_schema = BookSchema()

    def get(self, uuid=None):
        if not uuid:
            books = db.session.query(Book).all()
            return self.book_schema.dump(books, many=True), 200

        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if book:
            return self.book_schema.dump(book), 200

        return {'message': 'not found'}, 404

    def post(self):
        try:
            book = self.book_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400

        db.session.add(book)
        db.session.commit()
        return {'message': 'Created resource'}, 201

    def put(self, uuid):
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return {'message': 'not found'}, 404

        try:
            book = self.book_schema.load(request.json, instance=book, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400

        db.session.add(book)
        db.session.commit()
        return self.book_schema.dump(book), 200

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
