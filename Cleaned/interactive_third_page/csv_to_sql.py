#Needed???
#!rm customers.sqlite customers_cleaned.csv

# Dependencies
import pandas as pd
import numpy as np
import os

csvfile = "../SSA Baby Names by Decades.csv"

# Read CSV file into a pandas DataFrame
df = pd.read_csv(csvfile, dtype=object)

#df.head()

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Text, Float

# Create an engine to a SQLite database file called `babies.sqlite`
engine = create_engine("sqlite:///babies.sqlite")

# Create a connection to the engine called `conn`
conn = engine.connect()

# Use `declarative_base` from SQLAlchemy to model the demographics table as an ORM class
# Make sure to specify types for each column, e.g. Integer, Text, etc.
# http://docs.sqlalchemy.org/en/latest/core/type_basics.html
Base = declarative_base()

class Babies(Base):
    __tablename__ = 'babies'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    boy_name = Column(Text)
    num_boys=Column(Integer)
    girl_name = Column(Text)
    num_girls=Column(Integer)
   
    def __repr__(self):
        return f"id={self.id}, name={self.name}"