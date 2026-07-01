"""Ajout contract_type_id dans cv_works

Revision ID: 4a50bbb3e815
Revises: 640b6943b329
Create Date: 2026-07-01 15:28:15.785759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a50bbb3e815'
down_revision = '640b6943b329'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('cv_works', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contract_type_id',
                            sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_cv_works_contract_type',
            'cv_contracts',
            ['contract_type_id'],
            ['id'],
            onupdate='CASCADE',
            ondelete='CASCADE'
        )


def downgrade():
    with op.batch_alter_table('cv_works', schema=None) as batch_op:
        batch_op.drop_constraint(
            'fk_cv_works_contract_type', type_='foreignkey')
        batch_op.drop_column('contract_type_id')