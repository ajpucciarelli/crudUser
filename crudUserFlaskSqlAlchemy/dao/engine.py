import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///base.db', echo=True)

Base = declarative_base()

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()