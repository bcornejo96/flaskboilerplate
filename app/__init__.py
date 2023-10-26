from os import getenv
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from app.config import environment

FLASK_ENV = getenv('FLASK_ENV')
ENVIRONMENT = environment[FLASK_ENV]

app = Flask(__name__)
app.config.from_object(ENVIRONMENT)

authorizations = {
    #Authorization: Bearer {access_tokem}
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    app,
    title='Boilerplate Flask',
    version='0.1',
    description='Endpoints del boilerplate',
    doc='/swagger-ui',
    authorizations=authorizations
)


db = SQLAlchemy(app)

migrante = Migrate(app, db)

jwt = JWTManager(app)
mail = Mail(app)

