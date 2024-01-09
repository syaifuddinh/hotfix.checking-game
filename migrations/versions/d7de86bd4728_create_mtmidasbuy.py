"""create_mtmidasbuy

Revision ID: d7de86bd4728
Revises: ee4286780727
Create Date: 2024-01-04 23:02:10.982274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7de86bd4728'
down_revision: Union[str, None] = 'ee4286780727'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
	op.create_table(
		'MTMidasbuyGame',
		sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), nullable=False, unique=True, server_default=sa.text("uuid_generate_v4()")),
		sa.Column('midasbuySlug', sa.String(), nullable=False),
		sa.Column('gameSlug', sa.String(), nullable=False),
		sa.PrimaryKeyConstraint('id')
	)
	op.create_index('MTMidasbuyGame-GameSlugIndex', 'MTMidasbuyGame', ['gameSlug'], unique=False)


def downgrade() -> None:
    op.drop_table('MTMidasbuyGame')
