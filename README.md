# PHASE-3-PROJECT
## How to use it 
- This bank management system project performs the essential functions of banking software. It allows the user to:

1. View database records.
2. Create records.
3. Delete records.

## Technologies used
- python 
- pytest
- sqlalchemy

## Installation
1. Clone the repository.
git clone git@github.com:Vickme/BankmanagementPhase3CLIproject.git

2. Navigate to the project's directory:
cd BankmanagementPhase3CLIproject

3. Install all the required dependencies.

- To install Dependency and any other required libraries, run:
pipenv install

4. Enter the pipenv shell
pipenv shell

## Usage
- To launch the project follow these commands:
- cd lib
- python3 bank.py

- Use the following options to navigate through the main menu:

1. Press 'S' to view records.
2. Press 'F' to add new records.
3. Press 'R' to delete a customer and associated data.
4. Press 'Q' to quit the program.

### View Records Menu
- Customer Records
Press 'C' to see a list of all customers.

- Transaction Records
Press 'T' to see transaction records for a specific customer.

- Account Records
Press 'A' to see account records for a specific customer.

- Back to Main Menu
Press 'B' to return to the main menu.

### Add Records Menu
- Add a New Customer
Press 'C' to add a new customer.
Enter the first name and last name of the customer when prompted.

- Add a New Transaction
Press 'T' to add a new transaction.
Enter the required details for the transaction, such as the account ID, amount, and description (deposit or withdrawal).

- Add a New Account
Press 'A' to add a new account.
Provide the account type (savings or current), initial deposit, and customer ID.

- Back to Main Menu
Press 'B' to return to the main menu.

### Delete Customer
To delete a customer and their associated data:
Press 'R' in the main menu.
Enter the customer's ID when prompted.
Confirm the deletion.

## Author & License
The author of this software is Victor Mwangi Njutha.
