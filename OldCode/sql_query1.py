from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#import pandas as pd
#import numpy as np
#from sql_declarative import Base, Author, Citation
from sql_declarative import Base, AuthorsAndCitations
#from sqlalchemy import and_
#import matplotlib.pyplot as plt
#import seaborn as sns

engine = create_engine('sqlite:///scientists_linking.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


session.query(AuthorsAndCitations).all()

json = session.query(AuthorsAndCitations).first()
print (json.jsonstring)