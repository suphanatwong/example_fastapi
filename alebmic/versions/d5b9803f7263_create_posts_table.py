"""create posts table

Revision ID: d5b9803f7263
Revises: 03cf0c772383
Create Date: 2022-06-12 11:26:11.184133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5b9803f7263'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(),nullable=False, primary_key =True),
                    sa.Column('title', sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    
    pass
