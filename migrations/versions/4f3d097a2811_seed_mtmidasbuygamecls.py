"""seed_mtmidasbuygamecls

Revision ID: 4f3d097a2811
Revises: d7de86bd4728
Create Date: 2024-01-04 23:06:31.216612

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f3d097a2811'
down_revision: Union[str, None] = 'd7de86bd4728'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    	INSERT INTO "MTMidasbuyGame" ("midasbuySlug", "gameSlug") VALUES ('pubgm', 'pubg-mobile');
    	INSERT INTO "MTMidasbuyGame" ("midasbuySlug", "gameSlug") VALUES ('nikkegl', 'goddess-of-victory-nikke');
    ''')


def downgrade() -> None:
    op.execute('DELETE FROM "MTMidasbuyGame"')
