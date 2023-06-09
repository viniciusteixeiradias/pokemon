"""create pokemon table

Revision ID: 9129cf2eb935
Revises: 
Create Date: 2023-04-29 16:30:30.986937

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils as sau


# revision identifiers, used by Alembic.
revision = '9129cf2eb935'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sau.types.uuid.UUIDType(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon')
    # ### end Alembic commands ###
