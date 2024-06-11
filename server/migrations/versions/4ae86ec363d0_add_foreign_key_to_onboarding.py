"""add foreign key to onboarding

Revision ID: 4ae86ec363d0
Revises: 4b0705c93634
Create Date: 2024-06-11 12:01:00.289381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ae86ec363d0'
down_revision = '4b0705c93634'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_onboardings_employee_id_employees'), 'employees', ['employee_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_onboardings_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')

    # ### end Alembic commands ###
