"""empty message

Revision ID: d4c7203bf19c
Revises: 
Create Date: 2019-04-10 19:34:28.957803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4c7203bf19c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('country_code', sa.String(length=128), nullable=False),
    sa.Column('country_name', sa.String(length=128), nullable=True),
    sa.Column('continent', sa.String(length=128), nullable=True),
    sa.Column('region', sa.String(length=128), nullable=True),
    sa.Column('area', sa.Integer(), nullable=True),
    sa.Column('year_of_independence', sa.Integer(), nullable=True),
    sa.Column('population', sa.Float(), nullable=True),
    sa.Column('life_expectancy', sa.Float(), nullable=True),
    sa.Column('gnp', sa.Float(), nullable=True),
    sa.Column('gnpid', sa.Float(), nullable=True),
    sa.Column('alternative_name', sa.Text(), nullable=True),
    sa.Column('ruling_system', sa.Text(), nullable=True),
    sa.Column('founder', sa.Text(), nullable=True),
    sa.Column('iso_code', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('country_code'),
    sa.UniqueConstraint('country_code')
    )
    op.create_table('language',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country_code', sa.String(length=128), nullable=True),
    sa.Column('language', sa.String(length=128), nullable=True),
    sa.Column('percentage_of_use', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_name', sa.String(length=128), nullable=True),
    sa.Column('province', sa.String(length=128), nullable=True),
    sa.Column('population', sa.Float(), nullable=True),
    sa.Column('country_code', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['country_code'], ['country.country_code'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'CountryLanguage', 'country', ['country_code'], ['country_code'])
    op.create_foreign_key(None, 'CountryLanguage', 'language', ['language_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'CountryLanguage', type_='foreignkey')
    op.drop_constraint(None, 'CountryLanguage', type_='foreignkey')
    op.drop_table('city')
    op.drop_table('language')
    op.drop_table('country')
    # ### end Alembic commands ###
