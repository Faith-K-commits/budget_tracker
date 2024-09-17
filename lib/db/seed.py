import sys
import os

# Add the root directory of the project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from lib.db.models import User, Category, Transaction, Session

session = Session()

# Add some default categories
categories = ['Groceries', 'Rent', 'Utilities', 'Entertainment', 'Savings']
category_objects = []
for category_name in categories:
    category = Category(name=category_name)
    session.add(category)
    category_objects.append(category)

# Add a default user
user = User(username='admin')
session.add(user)

# Add some default transactions
transactions = [
    {'description': 'Grocery shopping', 'amount': 150.0, 'user': user, 'category': category_objects[0]},
    {'description': 'Monthly rent', 'amount': 1200.0, 'user': user, 'category': category_objects[1]},
    {'description': 'Electricity bill', 'amount': 100.0, 'user': user, 'category': category_objects[2]},
    {'description': 'Movie tickets', 'amount': 50.0, 'user': user, 'category': category_objects[3]},
    {'description': 'Savings deposit', 'amount': 500.0, 'user': user, 'category': category_objects[4]},
]

for transaction_data in transactions:
    transaction = Transaction(
        description=transaction_data['description'],
        amount=transaction_data['amount'],
        user=transaction_data['user'],
        category=transaction_data['category']
    )
    session.add(transaction)

# Commit the changes
session.commit()
print("Database seeded with initial data.")