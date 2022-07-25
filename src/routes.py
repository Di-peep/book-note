from flask import request
from flask_restful import Resource

from src import api


class Smoke(Resource):
    def get(self):
        return {'message': 'ok'}, 200


def get_books():
    return [
        {
            'id': '1',
            'title': 'Alice in Wonderland',
            'author': 'Lewis Carroll',
            'description': "Alice's Adventures in Wonderland is an 1865 novel written by English author"
                           " Charles Lutwidge Dodgson under the pseudonym Lewis Carroll. It tells of a girl"
                           " named Alice falling through a rabbit hole into a fantasy world populated by peculiar, "
                           "anthropomorphic creatures.",
            'year': '1865',
            'rating': '5.0'

        },
        {
            'id': '2',
            'title': 'Treasure Island',
            'author': 'Robert Louis Stevenson',
            'description': "Treasure Island is the ultimate pirate adventure story, replete with treasure and "
                           "an unforgettable cast, including Jim Hawkins, the boy at the centre of the action.",
            'year': '1883',
            'rating': '5.0'

        },
        {
            'id': '3',
            'title': 'The Adventures of Tom Sawyer',
            'author': 'Mark Twain',
            'description': "An 1876 novel about a young boy growing up along the Mississippi River. "
                           "It is set in the 1840s in the fictional town of St. Petersburg, "
                           "inspired by Hannibal, Missouri, where Twain lived as a boy. In the novel Tom Sawyer has "
                           "several adventures, often with his friend, Huck.",
            'year': '1876',
            'rating': '5.0'

        },
    ]


def get_book_by_uid(uid: str) -> dict:
    books = get_books()
    book = list(filter(lambda b: b['id'] == uid, books))
    return book[0] or {}


def create_book(book_json) -> list:
    books = get_books()
    book_json['id'] = str(int(books[-1]['id']) + 1)
    books.append(book_json)
    return books


class Books(Resource):
    def get(self, uid=None):

        if not uid:
            books = get_books()
            return books, 200

        book = get_book_by_uid(uid)
        if book:
            return book, 200

        return 'not found', 404

    def post(self):
        book_json = request.json
        return create_book(book_json), 201

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


api.add_resource(Smoke, '/smoke', '/smoke/', strict_slashes=False)
api.add_resource(Books, '/books', '/books/<uid>', strict_slashes=False)
