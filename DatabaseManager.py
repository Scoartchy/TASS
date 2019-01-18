import couchdb

#http_proxy=http://localhost:5984

#set http_proxy=http://127.0.0.1:5984

def CreateCouchDBDatabase():
    
    user = "admin"
    password = "admin"
    couchServer = couchdb.Server("http://%s:%s@couchdb:5984/" % (user, password))

    dbname = 'Scientists'   

    if dbname in couchServer:
        db = couchServer [dbname]
    else:
        db = couchServer.create(dbname)
        
    scientistsList = [
        { "Author": "Isaack Newton", "Quoters": ["Alber Einstein", "Stephen Hawking", "Nikola Tesla"]},
        { "Author": "James Clerk Maxwell", "Quoters": ["Max Planck", "Werner Heisenberg", "Richard Feynman"]},
    ]

    s = db.save(scientistsList)

    print(s)

    return

CreateCouchDBDatabase()
