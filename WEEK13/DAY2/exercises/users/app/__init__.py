import json
import os
import random
import flask_migrate
import flask_sqlalchemy
from flask import Flask, redirect, render_template, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from app.forms import LoginForm
from app.models import User

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


def generate_status():
    # Add random status to each user
    users = User.query.all()
    for user in users:
        user.status = random.choice(['admin', 'client'])
    db.session.commit()


# Call generate_status function to add random statuses to users in the database
generate_status()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data, city=form.city.data).first()
        if user is None:
            flash('User not found, please sign up.', 'error')
            return redirect(url_for('signup'))
        elif user.status == 'admin':
            return redirect(url_for('admin_index'))
        else:
            return redirect(url_for('client_index'))
    return render_template('login.html', form=form)


@app.route('/admin_index')
def admin_index():
    # Only show users with 'client' status to admin
    users = User.query.filter_by(status='client').all()
    return render_template('admin_index.html', users=users)


@app.route('/client_index')
def client_index():
    # Show user's own details to client
    user = User.query.filter_by(name=request.form['name'], city=request.form['city']).first()
    return render_template('client_index.html', user=user)
