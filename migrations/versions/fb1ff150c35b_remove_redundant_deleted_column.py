"""remove redundant deleted column

Revision ID: fb1ff150c35b
Revises: 127bf8e74ba0
Create Date: 2022-01-05 09:49:32.672185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb1ff150c35b'
down_revision = '127bf8e74ba0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card', 'deleted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('deleted', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
