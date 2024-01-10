"""TransactionTable

Revision ID: 75ff4e09cd25
Revises: 470cd58967e1
Create Date: 2024-01-10 12:24:03.202783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75ff4e09cd25'
down_revision = '470cd58967e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], name=op.f('fk_transactions_account_id_accounts')),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name=op.f('fk_transactions_customer_id_customers')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    # ### end Alembic commands ###
