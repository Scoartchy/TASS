
import couchdb

user = "EITIStudent"
password = "ERES2"
couchserver = couchdb.Server("http://%s:%s@couchdb:5984/" % (user, password)) #if there is account and password
#couch = couchdb.Server('http://localhost:5984')

dbname = 'scientistlinking'   #name of database

if dbname in couchserver:       #choose database to work with or create it  if not exist  
    db = couchserver [dbname]
else:
    db = couchserver.create(dbname)
    
example='Harry Nyquist'
example2 = 'Niels Bohr'

authors = {
       'name': example
       }

citations = {
        'whoisquoted': example2

       }

db.save(authors)
db.save(citations)

