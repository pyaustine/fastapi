"""add created_at columns to post table

Revision ID: 8d3e83a65cf3
Revises: 8b211654c5d4
Create Date: 2023-01-07 15:39:52.970560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d3e83a65cf3'
down_revision = '8b211654c5d4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'created_at')
    pass
