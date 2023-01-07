"""add few colums to post table

Revision ID: 8b211654c5d4
Revises: 0dcb0ebc8e52
Create Date: 2023-01-07 15:31:22.689062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b211654c5d4'
down_revision = '0dcb0ebc8e52'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    
    pass
