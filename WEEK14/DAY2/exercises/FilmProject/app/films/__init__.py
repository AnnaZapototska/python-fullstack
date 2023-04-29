from flask import Blueprint

films_bp = Blueprint('films', __name__, template_folder='templates', static_folder='static')

from app.films import routes


