from src import api
from src.resources.auth import RegisterUser, LoginUser
from src.resources.authors import Authors
from src.resources.books import Books
from src.resources.smoke import Smoke

api.add_resource(Smoke, '/smoke', '/smoke/', strict_slashes=False)
api.add_resource(Books, '/books', '/books/<uuid>', strict_slashes=False)
api.add_resource(Authors, '/authors', '/authors/<uuid>', strict_slashes=False)

api.add_resource(RegisterUser, '/register', strict_slashes=False)
api.add_resource(LoginUser, '/login', strict_slashes=False)
