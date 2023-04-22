from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


film_categories = db.Table('film_categories',
                           db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True),
                           db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True)
                           )

film_directors = db.Table('film_directors',
                          db.Column('director_id', db.Integer, db.ForeignKey('director.id'), primary_key=True),
                          db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True)
                          )

film_countries = db.Table('film_countries',
                          db.Column('country_id', db.Integer, db.ForeignKey('country.id'), primary_key=True),
                          db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True)
                          )

film_available_in_countries = db.Table('film_available_in_countries',
                                       db.Column('country_id', db.Integer, db.ForeignKey('country.id'),
                                                 primary_key=True),
                                       db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True)
                                       )


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, default=datetime.today)
    created_in_country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    created_in_country = db.relationship('Country', backref='films_created')
    available_in_countries = db.relationship('Country', secondary=film_available_in_countries,
                                             backref=db.backref('films_available', lazy='dynamic'))
    categories = db.relationship('Category', secondary=film_categories, backref=db.backref('films', lazy='dynamic'))
    directors = db.relationship('Director', secondary=film_directors, backref=db.backref('films', lazy='dynamic'))


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
