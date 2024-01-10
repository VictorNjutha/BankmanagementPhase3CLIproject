from models import Customer, Account, Transaction  # Adjust the import path if needed
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Create an SQLAlchemy session
engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind=engine)
session = Session()

def delete_customer_and_associated_data(customer_id):
    try:
        # Query the customer by their ID
        customer = session.query(Customer).filter(Customer.id == customer_id).first()

        if customer:
            # Query the accounts associated with the customer
            accounts_to_delete = session.query(Account).filter(Account.customer_id == customer.id).all()

            for account in accounts_to_delete:
                # Query and delete the transactions associated with each account
                transactions_to_delete = session.query(Transaction).filter(Transaction.account_id == account.id).all()
                for transaction in transactions_to_delete:
                    session.delete(transaction)

                # Delete the account itself
                session.delete(account)

            # Delete the customer
            session.delete(customer)

            # Commit the changes to the database
            session.commit()

            
        else:
            print(f"Customer with ID {customer_id} not found in the database.")

    except Exception as e:
        session.rollback()
        print("Error deleting customer and associated data:", e)

if __name__ == "__main__":
    customer_id_str = input("Enter the ID of the customer to delete: ").strip()
    
    try:
        customer_id = int(customer_id_str)
        delete_customer_and_associated_data(customer_id)
    except ValueError:
        print("Invalid customer ID. Please enter a valid integer.")