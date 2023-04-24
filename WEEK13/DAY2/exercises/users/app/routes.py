from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import User
from app.forms import LoginForm

@app.route('/')
def index():
    users = User.query.all()
    roscoeview_users = User.query.filter_by(city='Roscoeview').all()
    first_five_users = User.query.limit(5).all()
    starts_with_5_users = User.query.filter(User.zipcode.startswith('5')).all()
    return render_template('index.html', users=users, roscoeview_users=roscoeview_users,
                           first_five_users=first_five_users, starts_with_5_users=starts_with_5_users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data, address_city=form.address_city.data).first()
        if user:
            flash('You are now logged in!', 'success')
            if app.config['PART_III']:
                return redirect(url_for('add_user'))
            else: # this else is redundant, you can remove it because one line before you are doing return
                return redirect(url_for('index'))
        else:
            flash('Invalid name or address city. Please sign up!', 'danger')
            return redirect(url_for('signup'))
    return render_template('login.html', title='Login', form=form)


# @app.route('/index')
# def index():
#     user = User.query.filter_by(name=form.name.data, city=form.city.data).first()
#     if user.status == 'admin':
#         users = User.query.all()
#         return render_template('index.html', users=users)
#     else:
#         return render_template('index.html', user=user)
