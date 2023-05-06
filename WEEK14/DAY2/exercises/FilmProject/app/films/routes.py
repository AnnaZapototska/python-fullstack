import flask
from flask import render_template, redirect, url_for, request

from app import db
from app.films import films_bp
from app.films.forms import AddFilmForm, AddDirectorForm
from app.models import Film, Director, Country, Category


@films_bp.route('/homepage')
def film_homepage():
    return flask.render_template("homepage.html")


# @films_bp.route('/add_film', methods=['GET', 'POST'])
# def add_film():
#     form = AddFilmForm()
#     if form.validate_on_submit():
#         title = form.title.data
#         release_date = form.release_date.data
#         created_in_country = Country.query.first()  # for simplicity, set the first country as the created_in_country
#         film = Film(title=title, release_date=release_date, created_in_country=created_in_country)
#         db.session.add(film)
#         db.session.commit()
#         return redirect(url_for('films_bp.film_homepage'))
#     return render_template('film/addFilm.html', form=form)


@films_bp.route('/add_film', methods=['GET', 'POST'])
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        title = form.title.data
        release_date = form.release_date.data
        category = Category.query.get(1)  # assuming you have a Category instance with id=1
        country = form.country.data
        film = Film(title=title, release_date=release_date, created_in_country=country)
        film.film_categories.append(category)
        db.session.add(film)
        db.session.commit()
        return redirect(url_for('films.film_homepage'))

    categories = Category.query.all()
    countries = Country.query.all()
    return render_template('film/addFilm.html', form=form, categories=categories, countries=countries)


@films_bp.route('/add_director', methods=['GET', 'POST'])
def add_director():
    form = AddDirectorForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        director = Director(first_name=first_name, last_name=last_name)
        db.session.add(director)
        db.session.commit()
        return redirect(url_for('films.film_homepage'))
    return render_template('director/addDirector.html', form=form)
