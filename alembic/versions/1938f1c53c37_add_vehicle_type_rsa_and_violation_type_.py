"""add vehicle_type_rsa and violation_type_rsa

Revision ID: 1938f1c53c37
Revises: 1723862d5c0
Create Date: 2018-10-02 00:53:44.467726

"""

# revision identifiers, used by Alembic.
revision = '1938f1c53c37'
down_revision = '1723862d5c0'
branch_labels = None
depends_on = None

import sqlalchemy as sa

from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('markers', sa.Column('vehicle_type_rsa', sa.Text(), nullable=True))
    op.add_column('markers', sa.Column('violation_type_rsa', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('markers', 'violation_type_rsa')
    op.drop_column('markers', 'vehicle_type_rsa')
    ### end Alembic commands ###
