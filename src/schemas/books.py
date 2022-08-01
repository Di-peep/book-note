from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.database.models import Book


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        exclude = ['id']
        load_instance = True
