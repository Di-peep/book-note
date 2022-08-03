from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from src.database.models import Book


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        exclude = ['id']
        load_instance = True
        include_fk = True

    author = Nested('AuthorSchema', exclude=('books',))

