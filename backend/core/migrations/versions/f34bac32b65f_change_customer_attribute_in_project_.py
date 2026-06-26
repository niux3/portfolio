"""change customer attribute in project model

Revision ID: f34bac32b65f
Revises: 14ba5c7d4a3a
Create Date: 2026-06-26 17:31:29.179192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f34bac32b65f'
down_revision = '14ba5c7d4a3a'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('project_projects', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('customers_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_project_customer',              # Nom explicite de la contrainte
            'project_customers',                # Table référencée
            ['customers_id'],                   # Colonne locale
            ['id'],                             # Colonne référencée
            onupdate='CASCADE',
            ondelete='CASCADE'
        )
        batch_op.drop_column('customer')


def downgrade():
    with op.batch_alter_table('project_projects', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('customer', sa.VARCHAR(length=128), nullable=False))
        batch_op.drop_constraint('fk_project_customer', type_='foreignkey')
        batch_op.drop_column('customers_id')