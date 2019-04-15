"""empty message

Revision ID: 398de4f723c4
Revises: b6a4b6f45fc8
Create Date: 2019-04-12 09:37:07.818252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '398de4f723c4'
down_revision = 'b6a4b6f45fc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('language',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country_code', sa.String(length=128), nullable=True),
    sa.Column('language', sa.String(length=128), nullable=True),
    sa.Column('percentage_of_use', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'CountryLanguage', 'language', ['language_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'CountryLanguage', type_='foreignkey')
    op.drop_table('language')
    # ### end Alembic commands ###
