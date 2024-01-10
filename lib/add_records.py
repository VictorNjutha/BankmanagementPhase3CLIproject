from sqlalchemy.orm import sessionmaker
from models import Customer ,Account,Transaction # Adjust the import path


# Create an SQLAlchemy session
from sqlalchemy import create_engine

engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create a Customer object 
def add_customer_to_db(first_name, last_name):
    new_customer = Customer(first_name=first_name, last_name=last_name)
    session.add(new_customer)
    session.commit()
    return new_customer

def add_account_to_db(account_type,account_balance,customer_id):
    new_account = Account(customer_id=customer_id,account_balance=account_balance,account_type=account_type)
    session.add(new_account)
    session.commit()
    return new_account
def customer_exists(customer_id):
   
    customer = session.query(Customer).filter_by(id=customer_id).first()
    return customer is not None

def account_exists(account_id):
    account = session.query(Account).filter_by(id=account_id).first()
    return account is not None

def add_transaction_to_db(date,description,amount,customer_id,account_id):
    new_transaction = Transaction(date=date,description=description,amount=amount,customer_id=customer_id,account_id=account_id)
    session.add(new_transaction)
    session.commit()
    return new_transaction
def get_customer_id_and_balance_for_account(account_id):
    try:
        # Query the account by its ID
        account = session.query(Account).filter(Account.id == account_id).first()

        if account:
            # Return both the customer ID and the current account balance
            return account.customer_id, account.account_balance
        else:
            return None, None

    except Exception as e:
        print("Error getting customer ID and balance for account:", e)
        return None, None
def update_account_balance(account_id, new_balance):
    try:
        # Query the account by its ID
        account = session.query(Account).filter(Account.id == account_id).first()

        if account:
            # Update the account balance
            account.account_balance = new_balance
            session.commit()
        else:
            print(f"Account with ID {account_id} not found in the database.")

    except Exception as e:
        session.rollback()
        print("Error updating account balance:", e)    