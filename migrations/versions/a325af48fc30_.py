"""empty message

Revision ID: a325af48fc30
Revises: 1dc1d1539e97
Create Date: 2022-10-03 12:18:51.100271

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'a325af48fc30'
down_revision = '1dc1d1539e97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('application', 'user_input',
               existing_type=sa.VARCHAR(length=50000),
               type_=sqlalchemy_utils.types.encrypted.encrypted_type.StringEncryptedType(length=100000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('application', 'user_input',
               existing_type=sqlalchemy_utils.types.encrypted.encrypted_type.StringEncryptedType(length=100000),
               type_=sa.VARCHAR(length=50000),
               existing_nullable=True)
    # ### end Alembic commands ###
