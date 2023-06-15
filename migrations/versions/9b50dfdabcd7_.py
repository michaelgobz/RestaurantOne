"""empty message

Revision ID: 9b50dfdabcd7
Revises: ae8ee2ae27e9
Create Date: 2023-06-15 12:31:03.680536

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '9b50dfdabcd7'
down_revision = 'ae8ee2ae27e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=mssql.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=mssql.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
