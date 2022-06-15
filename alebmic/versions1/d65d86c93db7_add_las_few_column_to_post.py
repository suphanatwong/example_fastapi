"""add las few column to post

Revision ID: d65d86c93db7
Revises: e200e5d7b0a0
Create Date: 2022-06-12 23:28:58.695160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd65d86c93db7'
down_revision = 'e200e5d7b0a0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default = 'True'))
    op.add_column('posts', sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default = sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
