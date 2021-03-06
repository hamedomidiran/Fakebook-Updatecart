"""empty message

Revision ID: c3eaa7ed41db
Revises: 818ec15e3027
Create Date: 2021-02-18 13:37:19.438458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3eaa7ed41db'
down_revision = '818ec15e3027'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'cart', ['id'])
    op.create_unique_constraint(None, 'product', ['id'])
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'product', type_='unique')
    op.drop_constraint(None, 'cart', type_='unique')
    # ### end Alembic commands ###
