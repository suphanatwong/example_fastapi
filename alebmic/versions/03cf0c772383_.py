"""empty message

Revision ID: 03cf0c772383
Revises: 
Create Date: 2022-06-12 11:25:44.323649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03cf0c772383'
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

