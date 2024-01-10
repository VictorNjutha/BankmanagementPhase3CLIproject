from faker import Faker
import random
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Customer, Transaction, Account

fake = Faker()

# ...

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///bank.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Clear old data
    session.query(Customer).delete()
    session.query(Transaction).delete()
    session.query(Account).delete()
    session.commit()
    
    print("Seeding customers...")

    customers = [
        Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        for i in range(10)
    ]

    session.add_all(customers)
    session.commit()  # Commit the customers to get valid IDs

    print("Seeding accounts...")

    account_types = ["savings", "current"]

    accounts = [
        Account(
            account_type=random.choice(account_types),
            account_balance=random.randint(1, 10000000),
            customer_id=random.choice(customers).id
        )
        for i in range(30)
    ]

    session.add_all(accounts)
    session.commit()  # Commit the accounts to get valid IDs

    print("Seeding transactions...")

    transaction_types = ["deposit", "withdrawal"]

    transactions = []

    for i in range(100):
        customer = random.choice(customers)

        # Filter accounts to only include those belonging to the selected customer
        valid_accounts = [acc for acc in accounts if acc.customer_id == customer.id]

        if not valid_accounts:
            continue  # Skip this iteration if there are no valid accounts for the customer

        account = random.choice(valid_accounts)

        transaction = Transaction(
            date=fake.date_time_between(start_date="-1y", end_date="now"),
            amount=random.randint(1, 100000),  # Adjust the range as needed
            description=random.choice(transaction_types),
            customer_id=customer.id,
            account_id=account.id
        )

        transactions.append(transaction)

    session.add_all(transactions)

    try:
        session.commit()
        print("Data committed successfully.")
    except Exception as e:
        session.rollback()
        print("Error committing data:", e)