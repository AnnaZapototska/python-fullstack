from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


class AddFilmForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    release_date = DateField('Release Date', default=datetime.today())
    created_in_country = SelectField('Created In Country', coerce=int, validators=[DataRequired()])
    available_in_countries = SelectField('Available In Countries', coerce=int, validators=[DataRequired()], choices=[])
    categories = SelectField('Categories', coerce=int, validators=[DataRequired()], choices=[])
    directors = SelectField('Directors', coerce=int, validators=[DataRequired()], choices=[])
    submit = SubmitField('Add Film')


class AddDirectorForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Add Director')
