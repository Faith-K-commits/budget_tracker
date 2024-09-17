from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Model for users
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    transactions = relationship('Transaction', backref='user')

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

# Model for categories
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    transactions = relationship('Transaction', backref='category')

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name})"

# Model for transactions
class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    date = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"Transaction(id={self.id}, description={self.description}, amount={self.amount}, date={self.date})"

# Set up the database
engine = create_engine('sqlite:///budget_tracker.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
# session = Session()
# session.commit()
