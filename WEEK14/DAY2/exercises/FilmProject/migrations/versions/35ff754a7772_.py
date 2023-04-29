"""empty message

Revision ID: 35ff754a7772
Revises: 
Create Date: 2023-04-27 01:05:39.868593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35ff754a7772'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('director',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('film',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=False),
    sa.Column('created_in_country_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['created_in_country_id'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('films_categories',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['film.id'], ),
    sa.PrimaryKeyConstraint('film_id', 'category_id')
    )
    op.create_table('films_countries',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['film.id'], ),
    sa.PrimaryKeyConstraint('film_id', 'country_id')
    )
    op.create_table('films_directors',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('director_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['director_id'], ['director.id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['film.id'], ),
    sa.PrimaryKeyConstraint('film_id', 'director_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('films_directors')
    op.drop_table('films_countries')
    op.drop_table('films_categories')
    op.drop_table('film')
    op.drop_table('director')
    op.drop_table('country')
    op.drop_table('category')
    # ### end Alembic commands ###
