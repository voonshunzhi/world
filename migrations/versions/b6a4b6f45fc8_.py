"""empty message

Revision ID: b6a4b6f45fc8
Revises: d4c7203bf19c
Create Date: 2019-04-12 09:34:23.479972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6a4b6f45fc8'
down_revision = 'd4c7203bf19c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'country', ['country_code'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'country', type_='unique')
    # ### end Alembic commands ###
