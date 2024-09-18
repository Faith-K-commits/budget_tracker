# Budget Tracker CLI

## Project Description
This CLI-based budget tracker allows users to manage expenses and track them by category.
The application is built with Python using SQLAlchemy ORM for database interactions, allowing for easy querying and management of database records.

## Setup Instructions

1. Clone the repository.
2. Install dependencies with `pipenv install`.
3. Seed the database with initial data using `python lib/db/seed.py`.
4. Start the CLI application with `python lib/cli.py`.

## How to Use

The application presents a simple menu for interacting with the database:

### Menu Options
1. **Create User**: Add a new user by entering their username.
2. **Delete User**: Remove a user by specifying their user ID.
3. **Display Users**: View all users in the database.
4. **Find User**: Search for a user by username.
5. **Create Category**: Add a new category for a user.
6. **Delete Category**: Remove a category by its ID.
7. **Find Category by ID**: Search for a category using its ID.
8. **Display Categories**: View all categories in the database.
9. **Create Transaction**: Add a transaction for a user and category.
10. **Delete Transaction**: Remove a transaction by its ID.
11. **Display Transactions**: View all transactions in the database.
12. **Find Transaction by ID**: Search for a transaction by ID.
13. **View User Transactions**: Display all transactions for a specific user.
14. **Quit**: Exit the application.

### Example Workflow
1. Start the application.
2. Select **Create User** and enter a username.
3. Add categories for the user.
4. Create transactions under specific categories.
5. View or search for transactions by user or category.

## Models

### User
- `id`: Integer (Primary Key)
- `username`: String, unique, between 3 and 20 characters.

### Category
- `id`: Integer (Primary Key)
- `name`: String, between 3 and 50 characters.
- `user_id`: Foreign key (User).

### Transaction
- `id`: Integer (Primary Key)
- `description`: String, between 3 and 255 characters.
- `amount`: Float, positive values only.
- `user_id`: Foreign key (User).
- `category_id`: Foreign key (Category).
- `date`: DateTime, automatically set to current timestamp.

