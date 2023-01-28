"""removed username,password and email from model

Revision ID: d5659263b688
Revises: b7ff1eb91a70
Create Date: 2023-01-25 14:12:26.863828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5659263b688'
down_revision = 'b7ff1eb91a70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_username_key', 'user', type_='unique')
    op.drop_column('user', 'password')
    op.drop_column('user', 'email')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('password', sa.TEXT(), autoincrement=False, nullable=False))
    op.create_unique_constraint('user_username_key', 'user', ['username'])
    # ### end Alembic commands ###
