"""empty message

Revision ID: 322706553b27
Revises: b0133757d104
Create Date: 2022-05-08 15:24:38.064835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '322706553b27'
down_revision = 'b0133757d104'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('completed_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('task_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
