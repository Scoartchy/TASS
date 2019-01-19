import couchdb
import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def CreateCouchDBDatabase(scientists):
    
    print("-----------------------------------------------------------------------------------------------")
    print("Database works.")
    print("-----------------------------------------------------------------------------------------------")

    couchServer = couchdb.Server("http://localhost:5984")

    dbname = 'scientists'

    if dbname in couchServer:
        db = couchServer [dbname]
    else:
        db = couchServer.create(dbname)

    for scientist in scientists:
        s = Object()
        s.Author = scientist[1].decode('UTF8')

        quoters = []
        for q in scientist[2]:
            decodedQ = q.decode('UTF8')
            quoters.append(decodedQ)
        
        s.Quoters = quoters

        stringScientist = s.toJSON()
        print(stringScientist)
        jsonScientist = json.loads(stringScientist)
        db.save(jsonScientist)

    return

# TEST DATA
#inputScientist = "Isaac Newton"
#scientistName = inputScientist #.encode('UTF8')
#scientistHash = 11111
#scientists = [(scientistHash, scientistName, {"Albert Einstein", "Max Planck"})]

#CreateCouchDBDatabase(scientists)