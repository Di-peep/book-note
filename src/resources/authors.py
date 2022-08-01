from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.database.models import Author
from src.schemas.authors import AuthorSchema


class Authors(Resource):
    author_schema = AuthorSchema()

    def get(self, uuid=None):
        if not uuid:
            authors = db.session.query(Author).all()
            return self.author_schema.dump(authors, many=True), 200

        author = db.session.query(Author).filter_by(uuid=uuid).first()
        if author:
            return self.author_schema.dump(author), 200

        return {'message': 'not found'}, 404

    def post(self):
        try:
            author = self.author_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400

        db.session.add(author)
        db.session.commit()
        return {'message': 'Created resource'}, 201

    def put(self, uuid):
        author = db.session.query(Author).filter_by(uuid=uuid).first()
        if not author:
            return {'message': 'not found'}, 404

        try:
            author = self.author_schema.load(request.json, instance=author, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400

        db.session.add(author)
        db.session.commit()
        return self.author_schema.dump(author), 200

    def patch(self):
        pass

    def delete(self, uuid):
        author = db.session.query(Author).filter_by(uuid=uuid).first()
        if not author:
            return {'message': 'wrong data'}, 400

        db.session.delete(author)
        db.session.commit()
        return {'message': 'Resource was deleted'}, 204
