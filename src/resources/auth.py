import datetime
from functools import wraps

import jwt
from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

from src import db, app
from src.database.models import User
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


class LoginUser(Resource):
    def get(self):
        auth = request.authorization
        if not auth:
            return "No authorization", 401, {"WWW-Authenticate": "Basic realm='Authentication required'"}

        user = db.session.query(User).filter_by(username=auth.get('username', '')).first()
        if not user:
            return "No such user", 401, {"WWW-Authenticate": "Basic realm='Authentication required'"}

        if not check_password_hash(user.password, auth.get('password', '')):
            return "Wrong password", 401, {"WWW-Authenticate": "Basic realm='Authentication required'"}

        token = jwt.encode(
            {
                "user_id": user.uuid,
                "exp": datetime.datetime.now() + datetime.timedelta(hours=10)
            }, app.config['SECRET_KEY']
        )
        return jsonify({"token": token})


def token_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        token = request.headers.get('X-API-KEY', '')
        if not token:
            return "No token", 401, {"WWW-Authenticate": "Basic realm='Authentication required'"}

        try:
            uuid = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])['user_id']
        except (KeyError, jwt.ExpiredSignatureError):
            return "Bad token", 401, {"WWW-Authenticate": "Basic realm='Authentication required'"}

        user = db.session.query(User).filter_by(uuid=uuid).first()
        if not user:
            return "No such user", 401, {"WWW-Authenticate": "Basic realm='Authentication required'"}

        return func(self, *args, **kwargs)

    return wrapper
