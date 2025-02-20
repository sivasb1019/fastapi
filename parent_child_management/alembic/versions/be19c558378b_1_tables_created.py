"""1_tables created

Revision ID: be19c558378b
Revises: 
Create Date: 2024-07-14 17:51:55.780014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be19c558378b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('children', sa.Column('dob', sa.Date(), nullable=True))
    op.add_column('parents', sa.Column('dob', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('parents', 'dob')
    op.drop_column('children', 'dob')
    # ### end Alembic commands ###
