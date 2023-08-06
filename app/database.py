# start file contacts/app/database.py
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()


class ContactModel(Base):
    __tablename__ = "contacts"
    id = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)


def create_tables():
    Base.metadata.create_all(bind=engine)

# end of file contacts/app/database.py
