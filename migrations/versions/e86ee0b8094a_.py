"""empty message

Revision ID: e86ee0b8094a
Revises: eeb7e80aafc9
Create Date: 2020-11-07 17:56:33.904716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e86ee0b8094a'
down_revision = 'eeb7e80aafc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_checkin',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['staff_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_checkin')
    # ### end Alembic commands ###