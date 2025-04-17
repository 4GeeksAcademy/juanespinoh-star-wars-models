"""empty message

Revision ID: 4b227dc8d391
Revises: bd5deabbf475
Create Date: 2025-04-17 20:01:49.808287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b227dc8d391'
down_revision = 'bd5deabbf475'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('naves', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cargo_capacity', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('cost_in_credits', sa.Numeric(precision=5), nullable=False))
        batch_op.add_column(sa.Column('crew', sa.Numeric(precision=5), nullable=False))
        batch_op.add_column(sa.Column('length', sa.Numeric(precision=5, scale=2), nullable=False))
        batch_op.drop_constraint('naves_name_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('naves', schema=None) as batch_op:
        batch_op.create_unique_constraint('naves_name_key', ['name'])
        batch_op.drop_column('length')
        batch_op.drop_column('crew')
        batch_op.drop_column('cost_in_credits')
        batch_op.drop_column('cargo_capacity')

    # ### end Alembic commands ###
