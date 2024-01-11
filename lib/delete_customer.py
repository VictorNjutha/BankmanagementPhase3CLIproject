from models import Customer, Account, Transaction  
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind=engine)
session = Session()

def delete_customer_and_associated_data(customer_id):
    try:
        
        customer = session.query(Customer).filter(Customer.id == customer_id).first()

        if customer:
            
            accounts_to_delete = session.query(Account).filter(Account.customer_id == customer.id).all()

            for account in accounts_to_delete:
                
                transactions_to_delete = session.query(Transaction).filter(Transaction.account_id == account.id).all()
                for transaction in transactions_to_delete:
                    session.delete(transaction)

                
                session.delete(account)

            
            session.delete(customer)

            
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