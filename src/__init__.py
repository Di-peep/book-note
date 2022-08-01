from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

import config


app = Flask(__name__)
app.config.from_object(config.Config)

api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Book note"
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

from src import routes
from src.database import models
