import sys
import os

# Add the root directory of the project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.models import Session, User, Category, Transaction
from lib.helpers import display_menu

def main():
    session = Session()

    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip().lower()

        if choice == '1':
            create_user(session)
        elif choice == '2':
            delete_user(session)
        elif choice == '3':
            display_users(session)
        elif choice == '4':
            find_user_by_attribute(session)
        elif choice == '5':
            create_category(session)
        elif choice == '6':
            delete_category(session)
        elif choice == '7':
            find_category_by_id(session)
        elif choice == '8':
            display_categories(session)
        elif choice == '9':
            create_transaction(session)
        elif choice == '10':
            delete_transaction(session)
        elif choice == '11':
            display_transactions(session)
        elif choice == '12':
            find_transaction_by_id(session)
        elif choice == '13':
            view_user_transactions(session)
        elif choice == 'q':
            print("Exiting...")
            session.close()
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

def create_user(session):
    username = input("Enter username: ")
    if not username:
        print("Username cannot be empty.")
        return
    if session.query(User).filter_by(username=username).first():
        print("User with that username already exists.")
        return
    user = User(username=username)
    session.add(user)
    session.commit()
    print(f"User {username} created successfully.")

def delete_user(session):
    try:
        user_id = int(input("Enter user ID to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the user ID.")
        return
    user = session.get(User, user_id)
    if not user:
        print("User not found.")
        return
    session.delete(user)
    session.commit()
    print(f"User {user_id} deleted successfully.")

def display_users(session):
    users = session.query(User).all()
    if users:
        for user in users:
            print(user)
    else:
        print("No users to display")


def find_user_by_attribute(session):
    try:
        attribute = input("Enter the username to search for: ").strip().lower()
        if not attribute.strip():
            print("Username cannot be empty.")
            return
        user = session.query(User).filter_by(username=attribute).first()
        if user:
            print(f"User found: {user}")
        else:
            print("User not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_category(session):
    name = input("Enter category name: ")
    if not name:
        print("Category name cannot be empty.")
        return
    if session.query(Category).filter_by(name=name).first():
        print("Category with that name already exists.")
        return
    category = Category(name=name)
    session.add(category)
    session.commit()
    print(f"Category {name} created successfully.")

def delete_category(session):
    try:
        user_id = int(input("Enter user ID: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the user ID.")
        return
    user = session.get(User, user_id)
    if not user:
        print("User not found.")
        return

    categories = session.query(Category).join(Transaction).filter(Transaction.user_id == user_id).all()
    if not categories:
        print("No categories found for this user.")
        return

    print("Categories for user:")
    for category in categories:
        print(category)

    try:
        category_id = int(input("Enter category ID to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the category ID.")
        return
    category = session.get(Category, category_id)
    if not category:
        print("Category not found.")
        return

    session.delete(category)
    session.commit()
    print(f"Category {category_id} deleted successfully.")

def find_category_by_id(session):
    try:
        category_id = int(input("Enter category ID to search for: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the category ID.")
        return
    category = session.get(Category, category_id)
    if category:
        print(category)
    else:
        print("Category not found.")

def display_categories(session):
    categories = session.query(Category).all()
    if categories:
        for category in categories:
            print(category)
    else:
        print("No categories to display")

def create_transaction(session):
    description = input("Enter transaction description: ").strip()
    if not description:
        print("Transaction description cannot be empty.")
        return

    try:
        amount = float(input("Enter transaction amount: ").strip())
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError as e:
        print(f"Invalid amount: {e}")
        return

    user_id = int(input("Enter user ID: ").strip())
    category_id = int(input("Enter category ID: ").strip())
    user = session.get(User, user_id)
    category = session.get(Category, category_id)
    if not user:
        print("User not found.")
        return
    if not category:
        print("Category not found.")
        return

    transaction = Transaction(
        description=description,
        amount=amount,
        user=user,
        category=category
    )
    session.add(transaction)
    session.commit()
    print("Transaction created successfully.")


def delete_transaction(session):
    try:
        user_id = int(input("Enter user ID: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the user ID.")
        return
    user = session.get(User, user_id)
    if not user:
        print("User not found.")
        return

    transactions = session.query(Transaction).filter_by(user_id=user_id).all()
    if not transactions:
        print("No transactions found for this user.")
        return

    print("Transactions for user:")
    for transaction in transactions:
        print(transaction)

    try:
        transaction_id = int(input("Enter transaction ID to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the transaction ID.")
        return
    transaction = session.get(Transaction, transaction_id)
    if not transaction or transaction.user_id != user_id:
        print("Transaction not found or does not belong to this user.")
        return

    session.delete(transaction)
    session.commit()
    print(f"Transaction {transaction_id} deleted successfully.")

def display_transactions(session):
    transactions = session.query(Transaction).all()
    if transactions:
        for transaction in transactions:
            print(transaction)
    else:
        print("No transactions to display")

def find_transaction_by_id(session):
    try:
        transaction_id = int(input("Enter transaction ID to search for: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the transaction ID.")
        return
    transaction = session.get(Transaction, transaction_id)
    if transaction:
        print(transaction)
    else:
        print("Transaction not found.")

def view_user_transactions(session):
    try:
        user_id = int(input("Enter user ID: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the user ID.")
        return
    user = session.get(User, user_id)
    if not user:
        print("User not found.")
        return
    transactions = session.query(Transaction).filter_by(user_id=user_id).all()
    if transactions:
        for transaction in transactions:
            print(transaction)
    else:
        print("No transactions to display")

if __name__ == "__main__":
    main()
