from sqlalchemy.orm import sessionmaker
from models import Customer, Transaction, Account

from sqlalchemy import create_engine

# Create an SQLAlchemy session
engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind=engine)
session = Session()

def list_all_customers():
    customers = session.query(Customer).all()
    if customers:
        print("List of All Customers:")
        for customer in customers:
            print(f"Customer ID: {customer.id}, Name: {customer.first_name} {customer.last_name}")
    else:
        print("No customers found in the database.")


# Function to list accounts for a specific customer
def list_accounts_for_customer(customer_id):
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        accounts = session.query(Account).filter(Account.customer_id == customer_id).all()
        if accounts:
            print(f"Accounts for Customer ID {customer.id}:")
            for account in accounts:
                print(f"Account ID: {account.id}, Type: {account.account_type}, Balance: {account.account_balance}")
        else:
            print(f"No accounts found for Customer ID {customer.id}.")
    else:
        print("Customer not found.")

# Function to list transactions for a specific customer
def list_transactions_for_customer(customer_id):
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        transactions = session.query(Transaction).filter(Transaction.customer_id == customer_id).all()
        if transactions:
            print(f"Transactions for Customer ID {customer.id}:")
            for transaction in transactions:
                print(f"Transaction ID: {transaction.id}, Description: {transaction.description}, Amount: {transaction.amount}")
        else:
            print(f"No transactions found for Customer ID {customer.id}.")
    else:
        print("Customer not found.")

# Example usage of the functions
if __name__ == "__main__":
    list_accounts_for_customer(1)  # Replace 1 with the desired customer ID
    list_transactions_for_customer(1)  # Replace 1 with the desired customer ID
    list_all_customers()