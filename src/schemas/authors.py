from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from src.database.models import Author


class AuthorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        exclude = ['id']
        load_instance = True
        include_fk = True

    books = Nested('BookSchema', many=True, exclude=('author',))
