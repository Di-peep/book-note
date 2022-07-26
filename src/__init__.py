from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import config


app = Flask(__name__)
app.config.from_object(config.Config)

api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src import routes, models
