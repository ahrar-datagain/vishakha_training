"""Initial migration

Revision ID: 7526ecbb620e
Revises: 
Create Date: 2024-09-09 12:57:21.049729

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7526ecbb620e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_my_table_id'), 'my_table', ['id'], unique=False)
    op.create_index(op.f('ix_my_table_name'), 'my_table', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_my_table_name'), table_name='my_table')
    op.drop_index(op.f('ix_my_table_id'), table_name='my_table')
    op.drop_table('my_table')
    # ### end Alembic commands ###
