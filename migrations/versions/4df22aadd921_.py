"""empty message

Revision ID: 4df22aadd921
Revises: e4c91c5a45af
Create Date: 2023-03-21 14:44:36.227551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4df22aadd921'
down_revision = 'e4c91c5a45af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users_address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_address',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('address_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], name='users_address_address_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='users_address_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='users_address_pkey')
    )
    op.drop_table('users_addresses')
    # ### end Alembic commands ###