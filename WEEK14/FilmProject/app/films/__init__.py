import os

import flask_migrate
import flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_info = {'host': 'localhost',
           'database': 'films',
           'psw': '1234',
           'user': 'postgres',
           'port': ''}

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SECRET_KEY'] = "333"

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from app.films import routs, models
