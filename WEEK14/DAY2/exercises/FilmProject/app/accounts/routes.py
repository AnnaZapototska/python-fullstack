
import flask

from app.accounts import accounts_bp


@accounts_bp.route("/")
def index():
    return flask.render_template("accounts_main.html")