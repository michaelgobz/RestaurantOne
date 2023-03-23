"""empty message

Revision ID: 8bdf02f65089
Revises: 8483aceda389
Create Date: 2023-03-22 17:22:29.467204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bdf02f65089'
down_revision = '8483aceda389'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('verification_tokens',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('token', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token_id', sa.String(length=50), nullable=True))
        batch_op.create_foreign_key(None, 'verification_tokens', ['token_id'], ['id'], use_alter=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('token_id')

    op.drop_table('verification_tokens')
    # ### end Alembic commands ###