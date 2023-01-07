"""create posts table

Revision ID: aa8b96e8eef9
Revises: 
Create Date: 2023-01-07 14:38:25.679309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa8b96e8eef9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
