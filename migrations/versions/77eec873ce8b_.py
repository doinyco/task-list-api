"""empty message

Revision ID: 77eec873ce8b
Revises: ea5a97f9912f
Create Date: 2022-05-12 21:20:26.695168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77eec873ce8b'
down_revision = 'ea5a97f9912f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title2', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title2')
    # ### end Alembic commands ###
