from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    address_city = StringField('Address City', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Login')
