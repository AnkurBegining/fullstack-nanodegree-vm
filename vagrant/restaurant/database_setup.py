import sys
from sqlalchemy import Integer, String, column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationships
from sqlalchemy import create_engine

Base = declarative_base()


#### Insert at the end of file #####
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metdata.create_all(engine)
