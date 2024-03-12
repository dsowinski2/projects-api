"""empty message

Revision ID: 6b02984ab58b
Revises:
Create Date: 2024-03-12 09:48:02.892657

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "6b02984ab58b"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "project",
        sa.Column("id", sa.Integer, autoincrement=True, primary_key=True),
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("date_start", sa.DateTime, nullable=False),
        sa.Column("date_end", sa.DateTime, nullable=False),
        sa.Column("geo_json", sa.JSON, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("project")
