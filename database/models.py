from database import Base
from sqlalchemy import Column, String, Float, Boolean, Date, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    phone_number = Column(Integer, nullable=False)
    name = Column(String, nullable=False)

    reg_date = Column(DateTime)

class Password(Base):
    __tablename__ = 'user_password'
    user_id =Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    password = Column(String, nullable=False)
    pincode = Column(Integer)

    user_fk = relationship(User)

class Card(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    card_number = Column(Integer, nullable=False)
    card_name = Column(String)
    cardholder = Column(String)
    exp_date = Column(Integer, nullable=False)
    balance = Column(Float)

    added_date = Column(DateTime)

    user_fk = relationship(User)

class Payment(Base):
    __tablename__ = 'payment'
    payment_id = Column(Integer, autoincrement=True, primary_key=True)
    card_id = Column(Integer, ForeignKey('cards.card_id'))
    amount = Column(Float, nullable=False)
    card_to = Column(Integer, nullable=False)

    paymnet_date = Column(DateTime)

    card_fk = relationship(Card)

class ServiceCategory(Base):
    __tablename__ = 'service_category'
    category_id = Column(Integer, autoincrement=True, primary_key=True)
    category_name = Column(String, nullable=False)

    added_date = Column(DateTime)

class Service(Base):
    __tablename__ = 'services'
    service_id = Column(Integer, autoincrement=True, primary_key=True)
    service_category = Column(Integer, ForeignKey('service_category.category_id'))
    sservice_name = Column(String, nullable=False)
    service_balance = Column(Float)
    service_check = Column(Integer, nullable=False)

    reg_date = Column(DateTime)

    category_fk = relationship(ServiceCategory)