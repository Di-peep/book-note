from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.database.models import Author


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        exclude = ['id']
        load_instance = True
