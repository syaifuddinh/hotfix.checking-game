"""seed_midasbuy_availability

Revision ID: ee4286780727
Revises: fb5b796fab58
Create Date: 2024-01-04 22:45:35.647610

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee4286780727'
down_revision: Union[str, None] = 'fb5b796fab58'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    	UPDATE "MTGame" SET "hasMidasbuy" = True WHERE slug = 'pubg-mobile' ;
    	UPDATE "MTGame" SET "hasMidasbuy" = True WHERE slug = 'goddess-of-victory-nikke' ;
    ''')


def downgrade() -> None:
    pass
