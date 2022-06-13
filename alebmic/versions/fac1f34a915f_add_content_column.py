"""add content column

Revision ID: fac1f34a915f
Revises: 03cf0c772383
Create Date: 2022-06-12 20:24:18.069348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fac1f34a915f'
down_revision = '03cf0c772383'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(),nullable =False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
