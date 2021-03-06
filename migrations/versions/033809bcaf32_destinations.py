"""destinations

Revision ID: 033809bcaf32
Revises: 4a77b8fb792a
Create Date: 2017-08-24 05:56:45.166590

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = '033809bcaf32'
down_revision = '4a77b8fb792a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('destinations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('point', geoalchemy2.types.Geometry(geometry_type='POINT'), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('address', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('destinations')
    # ### end Alembic commands ###
