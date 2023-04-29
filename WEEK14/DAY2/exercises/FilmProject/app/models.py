from datetime import datetime
from app import db

films_categories = db.Table('films_categories',
                            db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True),
                            db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
                            )

films_countries = db.Table('films_countries',
                           db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True),
                           db.Column('country_id', db.Integer, db.ForeignKey('country.id'), primary_key=True)
                           )

films_directors = db.Table('films_directors',
                           db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True),
                           db.Column('director_id', db.Integer, db.ForeignKey('director.id'), primary_key=True)
                           )


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    films_created = db.relationship('Film', backref='country_created', lazy=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    film_categories = db.relationship('Film', secondary=films_categories, backref='film_categories', lazy=True)


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    directed_films = db.relationship('Film', secondary=films_directors, backref='directors', lazy=True)


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    created_in_country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    created_in_country = db.relationship('Country')

    available_in_countries = db.relationship('Country', secondary=films_countries, backref='available_films', lazy=True)

    film_categories = db.relationship('Category', secondary=films_categories, backref='categories', lazy=True)

    directors = db.relationship('Director', secondary=films_directors, backref='films', lazy=True)
