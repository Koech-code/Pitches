"""Initial Migration

Revision ID: 3315ca3c6613
Revises: 79035981ac59
Create Date: 2021-08-17 15:02:36.725139

"""

# revision identifiers, used by Alembic.
revision = '3315ca3c6613'
down_revision = '79035981ac59'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('post', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###