
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
#from sql_declarative import Base, Author, Citation
from sql_declarative import Base, AuthorsAndCitations
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
 
json2= {                                                    ##SCRAPPED JSON
    "author":("Albert Einstein", "Niels Bohr"),
    "quotingperson": ("Pierre Curie", "Hendrik Lorentz")
    }
  
new_authorsAndCitations = = AuthorsAndCitations(jsonstring=json2)   ##SCRAPPED JSON
session.add(new_authorsAndCitations)
session.commit()


