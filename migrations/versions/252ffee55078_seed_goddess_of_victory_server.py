"""seed_goddess_of_victory_server

Revision ID: 252ffee55078
Revises: 95b32b136977
Create Date: 2024-01-07 17:34:29.963209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '252ffee55078'
down_revision: Union[str, None] = '95b32b136977'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    	INSERT INTO "MTServer"("gameSlug", "serverSlug", "serverName", "midasbuyIndex") VALUES( 'goddess-of-victory-nikke', 'kr', 'KR', '1' );
		INSERT INTO "MTServer"("gameSlug", "serverSlug", "serverName", "midasbuyIndex") VALUES( 'goddess-of-victory-nikke', 'jp', 'JP', '2' );
		INSERT INTO "MTServer"("gameSlug", "serverSlug", "serverName", "midasbuyIndex") VALUES( 'goddess-of-victory-nikke', 'global', 'Global', '3' );
		INSERT INTO "MTServer"("gameSlug", "serverSlug", "serverName", "midasbuyIndex") VALUES( 'goddess-of-victory-nikke', 'sea', 'SEA', '4' );
		INSERT INTO "MTServer"("gameSlug", "serverSlug", "serverName", "midasbuyIndex") VALUES( 'goddess-of-victory-nikke', 'na', 'NA', '5' );
    ''')


def downgrade() -> None:
    op.execute('DELETE FROM "MTServer" WHERE "gameSlug" = \'goddess-of-victory-nikke\'')
