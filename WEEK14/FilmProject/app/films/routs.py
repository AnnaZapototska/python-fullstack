from flask import render_template, redirect, url_for
from app.films import app, db
from app.films.forms import AddFilmForm, AddDirectorForm
from .models import Film, Director, Country, Category


@app.route('/homepage')
def homepage():
    films = Film.query.all()
    directors = Director.query.all()
    return render_template('partial/homepage.html', films=films, directors=directors)


@app.route('/add-film', methods=['GET', 'POST'])
def add_film():
    form = AddFilmForm()
    form.created_in_country.choices = [(c.id, c.name) for c in Country.query.all()]
    form.available_in_countries.choices = [(c.id, c.name) for c in Country.query.all()]
    form.categories.choices = [(c.id, c.name) for c in Category.query.all()]
    form.directors.choices = [(d.id, f"{d.first_name} {d.last_name}") for d in Director.query.all()]
    if form.validate_on_submit():
        film = Film(title=form.title.data, release_date=form.release_date.data)
        film.created_in_country_id = form.created_in_country.data
        film.available_in_countries = Country.query.filter(Country.id.in_(form.available_in_countries.data)).all()
        film.categories = Category.query.filter(Category.id.in_(form.categories.data)).all()
        film.directors = Director.query.filter(Director.id.in_(form.directors.data)).all()
        db.session.add(film)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template('film/addFilm.html', form=form)

@app.route('/add-director', methods=['GET', 'POST'])
def add_director():
    form = AddDirectorForm()
    if form.validate_on_submit():
        director = Director(first_name=form.first_name.data, last_name=form.last_name.data)
        db.session.add(director)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template('directors/addDirectors.html', form=form)
