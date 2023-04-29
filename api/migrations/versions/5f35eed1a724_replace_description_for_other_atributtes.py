"""replace description for other atributtes

Revision ID: 5f35eed1a724
Revises: 9129cf2eb935
Create Date: 2023-04-29 19:25:49.503767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f35eed1a724'
down_revision = '9129cf2eb935'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon', sa.Column('base_experience', sa.Integer(), nullable=False))
    op.add_column('pokemon', sa.Column('height', sa.Integer(), nullable=False))
    op.add_column('pokemon', sa.Column('weight', sa.Integer(), nullable=False))
    op.drop_column('pokemon', 'description')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon', sa.Column('description', sa.VARCHAR(), nullable=False))
    op.drop_column('pokemon', 'weight')
    op.drop_column('pokemon', 'height')
    op.drop_column('pokemon', 'base_experience')
    # ### end Alembic commands ###