"""add fkey to post table

Revision ID: 0dcb0ebc8e52
Revises: e0b2ed2156b1
Create Date: 2023-01-07 15:24:38.945149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dcb0ebc8e52'
down_revision = 'e0b2ed2156b1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
