from app import db
from app.models import Category, Country, Director, Film

# create some countries
usa = Country(name='USA')
uk = Country(name='UK')

# create some categories
action = Category(name='Action')
comedy = Category(name='Comedy')

# create some directors
spielberg = Director(first_name='Steven', last_name='Spielberg')
tarantino = Director(first_name='Quentin', last_name='Tarantino')

# create some films
film1 = Film(title='Jurassic Park', created_in_country=usa, release_date='1993-06-11', directors=[spielberg], film_categories=[action])
film2 = Film(title='Pulp Fiction', created_in_country=usa, release_date='1994-05-21', directors=[tarantino], film_categories=[comedy])

# add the objects to the session and commit the changes to the database
db.session.add_all([usa, uk, action, comedy, spielberg, tarantino, film1, film2])
db.session.commit()
