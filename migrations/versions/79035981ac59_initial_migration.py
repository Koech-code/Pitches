"""Initial Migration

Revision ID: 79035981ac59
Revises: 735c3e1f9d7a
Create Date: 2021-08-17 14:54:23.361641

"""

# revision identifiers, used by Alembic.
revision = '79035981ac59'
down_revision = '735c3e1f9d7a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###