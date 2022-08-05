from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from src import db
from src.schemas.users import UserSchema


class RegisterUser(Resource):
    user_schema = UserSchema()

    def post(self):
        try:
            user = self.user_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "Such user exists"}, 409

        return self.user_schema.dump(user), 201
