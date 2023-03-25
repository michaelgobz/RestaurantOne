"""empty message

Revision ID: 4914ecd5a42f
Revises: d4770801482a
Create Date: 2023-03-25 14:03:05.108070

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4914ecd5a42f'
down_revision = 'd4770801482a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menu_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=50), nullable=False))
        batch_op.alter_column('duration_of_preparation',
                              existing_type=postgresql.TIMESTAMP(),
                              type_=sa.Integer(),
                              nullable=False
                              )

    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.alter_column('price',
                              existing_type=sa.REAL(),
                              type_=sa.Float(precision=2),
                              existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.alter_column('price',
                              existing_type=sa.Float(precision=2),
                              type_=sa.REAL(),
                              existing_nullable=False)

    with op.batch_alter_table('menu_items', schema=None) as batch_op:
        batch_op.alter_column('duration_of_preparation',
                              existing_type=sa.Integer(),
                              type_=postgresql.TIMESTAMP(),
                              nullable=True)
        batch_op.drop_column('category')

    # ### end Alembic commands ###