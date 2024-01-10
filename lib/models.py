from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Float, create_engine, Date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    
    accounts = relationship("Account", back_populates="customer")
    transactions = relationship("Transaction", back_populates="customer")
    
    def __repr__(self):
        return f"{self.id},name:{self.first_name}{self.last_name}"

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.now)
    description = Column(String)
    amount = Column(Float)
    
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)  # Add nullable=False
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)  # Add nullable=False
    
    account = relationship("Account", back_populates="transactions")
    customer = relationship("Customer", back_populates="transactions")
    
    def __repr__(self):
        return f"{self.id},date:{self.date},description:{self.description},amount:{self.amount}"

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    account_type = Column(String)
    account_balance = Column(Float)
    
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)  # Add nullable=False
    
    customer = relationship("Customer", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")
    
    def __repr__(self):
        return f"{self.id}, Account type:{self.account_type}, Account balance:{self.account_balance}"
   
        