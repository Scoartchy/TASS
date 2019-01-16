
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from sql_declarative import Base, Author, Citation
#import math
engine = create_engine('sqlite:///scientists_linking.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Insert an Author in the person table
#df_authors = pd.read_csv('Authors.csv')
#for row in df_authors.iterrows():
#    new_author = Author(name=row[1][1])
#    session.add(new_author)
#    session.commit()
#
#df_citations = pd.read_csv('Citations.csv')
#for row in df_citations.iterrows():
#    new_citation = Citation(whoIsQuoted=row[1][1],
#                           whoIsQuoting=row[1][2])
#    session.add(new_citation)
#    session.commit()

new_author = Author(name='albert fettel')
session.add(new_author)
session.commit()