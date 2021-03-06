"""Initial Migration

Revision ID: 1e44b9d888b9
Revises: 212983c96341
Create Date: 2021-08-19 16:46:21.527036

"""

# revision identifiers, used by Alembic.
revision = '1e44b9d888b9'
down_revision = '212983c96341'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
