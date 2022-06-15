"""add fk to post

Revision ID: e200e5d7b0a0
Revises: 7265c26ca9ce
Create Date: 2022-06-12 22:42:19.802763

"""
from alembic import op
from fastapi import FastAPI
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e200e5d7b0a0'
down_revision = '7265c26ca9ce'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id', sa.Integer(),nullable =False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
    local_cols=[
                     'owner_id'],remote_cols=['id'],ondelete="CASCADE")

    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts','owner_id')
    pass
