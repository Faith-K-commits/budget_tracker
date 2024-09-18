from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Model for users
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    _username = Column("username", String, nullable=False, unique=True)

    transactions = relationship('Transaction', backref='user')

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Username cannot be empty.")
        if not (3 <= len(value) <= 20):
            raise ValueError("Username must be between 3 and 20 characters long.")
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric (letters and numbers only).")
        self._username = value

# Model for categories
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', backref='categories')
    transactions = relationship('Transaction', backref='category')

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name}, user_id={self.user_id})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Category name cannot be empty.")
        if not (3 <= len(value) <= 50):
            raise ValueError("Category name must be between 3 and 50 characters long.")
        self._name = value

# Model for transactions
class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    _description = Column("description", String, nullable=False)
    _amount = Column("amount", Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"Transaction(id={self.id}, description={self.description}, amount={self.amount}, date={self.date})"

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Transaction description cannot be empty.")
        if not (3 <= len(value) <= 255):
            raise ValueError("Transaction description must be between 3 and 255 characters long.")
        self._description = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value <= 0:
            raise ValueError("Transaction amount must be greater than 0.")
        self._amount = value

# Set up the database
engine = create_engine('sqlite:///budget_tracker.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
