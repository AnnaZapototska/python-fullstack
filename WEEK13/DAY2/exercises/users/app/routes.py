from flask import render_template
from app import app, db
from app.models import User

@app.route('/')
def index():
    users = User.query.all()
    roscoeview_users = User.query.filter_by(city='Roscoeview').all()
    first_five_users = User.query.limit(5).all()
    starts_with_5_users = User.query.filter(User.zipcode.startswith('5')).all()
    return render_template('index.html', users=users, roscoeview_users=roscoeview_users,
                           first_five_users=first_five_users, starts_with_5_users=starts_with_5_users)
