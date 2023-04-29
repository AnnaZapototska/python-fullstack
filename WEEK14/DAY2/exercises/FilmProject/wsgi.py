from flask import Flask
# from app.accounts import accounts_bp
# from app.films import films_bp
#
# flask_app = Flask(__name__)
# flask_app.register_blueprint(accounts_bp)
# flask_app.register_blueprint(films_bp)
from app import flask_app

if __name__ == "__main__":
    flask_app.run()
