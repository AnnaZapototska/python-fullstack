import os

import flask_migrate
import flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_info = {'host': 'localhost',
           'database': 'robots',
           'psw': '1234',
           'user': 'postgres',
           'port': ''}

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SECRET_KEY'] = "211"

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from app import routes, models

import json


def populate():
    with app.app_context():
        from app.models import User

        with open('app/users.json') as f:
            users = json.load(f)

        for user in users:
            new_user = User(name=user['name'], street=user['address']['street'], city=user['address']['city'],
                            zipcode=user['address']['zipcode'])
            db.session.add(new_user)

        db.session.commit()


populate()
