"""empty message

Revision ID: 6b02984ab58b
Revises: 
Create Date: 2024-03-12 09:48:02.892657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b02984ab58b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "project",
        sa.Column("id", sa.Integer, autoincrement=True, primary_key=True)
    )


def downgrade() -> None:
    op.drop_table("project")
