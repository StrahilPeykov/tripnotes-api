"""Change date to trip_date in Trip model

Revision ID: dfd0e158e606
Revises: 9ff9bc009d2a
Create Date: 2025-03-24 18:07:32.572799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfd0e158e606'
down_revision: Union[str, None] = '9ff9bc009d2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trips', sa.Column('trip_date', sa.Date(), nullable=True))
    op.drop_column('trips', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trips', sa.Column('date', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_column('trips', 'trip_date')
    # ### end Alembic commands ###
