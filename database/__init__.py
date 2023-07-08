from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "sqlite:///pay_test.db"
# connect_args={"check_name_thread": False} - только для sqlite3
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# gen подкл to base
def get_db():
    session = SessionLocal()
    try:
         yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()

from database.userservice import *
from database.cardservice import *
from database.paymentservice import *
from database.userservice import *