"""empty message

Revision ID: ecc4b49a5664
Revises: a325af48fc30
Create Date: 2022-10-06 15:08:00.819433

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'ecc4b49a5664'
down_revision = 'a325af48fc30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('application', sa.Column('number_sessions', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('application', 'number_sessions')
    # ### end Alembic commands ###
