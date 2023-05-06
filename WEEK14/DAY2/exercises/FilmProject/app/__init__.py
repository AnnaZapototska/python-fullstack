from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_wtf import CSRFProtect


flask_app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

csrf = CSRFProtect(flask_app)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://newuser:newpassword@localhost/films'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flask_app.config['SECRET_KEY'] = 'bbtGut-ZfXkZ1Ea_VXj88ngAxdW6vnYrU2soteY-qBk'
flask_app.config['DEBUG'] = True

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

from app.films import films_bp
from app.accounts import accounts_bp

flask_app.register_blueprint(films_bp, url_prefix='/films')
flask_app.register_blueprint(accounts_bp, url_prefix='/accounts')
