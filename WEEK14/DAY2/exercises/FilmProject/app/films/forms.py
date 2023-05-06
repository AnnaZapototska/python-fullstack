from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField
from wtforms.validators import DataRequired
from wtforms_alchemy import QuerySelectField

from app.models import Category, Country


class AddFilmForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    release_date = DateField('Release Date', validators=[DataRequired()])
    category = QuerySelectField('Category', validators=[DataRequired()], query_factory=lambda: Category.query.all())
    country = QuerySelectField('Country', validators=[DataRequired()], query_factory=lambda: Country.query.all())


class AddDirectorForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
