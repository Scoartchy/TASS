##create graph
import json
import networkx as nx
import couchdb
#MultiGraph.to_undirected(as_view=False)

def BuildGraph(jsonIN):   #Build all data graph

    # convert into JSON:
    convert = json.dumps(jsonIN)
    
    # the result is a JSON string:
    jsonloads = json.loads(convert)
    
    if type(jsonloads["Author"]) == list:   #add author nodes, several authors
        G.add_nodes_from(jsonloads["Author"])
    elif type(jsonloads["Author"]) == str:  #add author nodes, one author
        G.add_node(jsonloads["Author"])
    else:
        print ("")

    if type(jsonloads["Quoters"]) == list:         ##add quoting nodes, several citations
        G.add_nodes_from(jsonloads["Quoters"])
        
    elif type(jsonloads["Quoters"]) == str:       #add quoting node, one citation
        G.add_node(jsonloads["Quoters"])
    else:
        print ("")
        
        
        
    if type(jsonloads["Author"]) == list:   #draw edges
        
        if type(jsonloads["Quoters"]) == str:             #several authors, one citation
            for x in jsonloads["Author"]:
                G.add_edges_from([(x, jsonloads["Quoters"])])
        
        elif type(jsonloads["Quoters"]) == list:          #several authors, several citations
           for x in jsonloads["Quoters"]:
               for y in jsonloads["Author"]:
                   G.add_edge(y, x)


    elif type(jsonloads["Author"]) == str:
        
        if type(jsonloads["Quoters"]) == str:             #one author, one citation
            G.add_edges_from([(jsonloads["Author"], jsonloads["Quoters"])])
        
        elif type(jsonloads["Quoters"]) == list:          #one author, several citation
            for x in jsonloads["Quoters"]:
                G.add_edges_from([(jsonloads["Author"], x)])


G = nx.Graph()
H = nx.Graph()

couchServer = couchdb.Server("http://localhost:5984")
idtable=[]
dbname = 'scientistssimr'
db = couchServer[dbname]
#                                           
#for docuid in db.view('_all_docs'):     #To make all data graph
#    
#    i = docuid['id']
#    jsonOUT = db[i]
#    BuildGraph(jsonOUT)     #add nodes and edges
##    
#nx.draw(G,pos=nx.spring_layout(H))

for docid in db.view('_all_docs'):
    
    i = docid['id']
    jsonOUT = db[i]

    Aut=db[i]["Author"]

    for quoter in (db[i]["Quoters"]):

        for articles in db.view('_all_docs'):  ##search quoter in autors
            j=articles['id']
            if db[j]["Author"] == quoter:    ##quoter is an author in database
                
                for quot in db[j]["Quoters"]: #search author in qouters of quoter
                    if quot == Aut:
                        H.add_node(quot)
                        H.add_node(Aut)
                        H.add_edge(Aut, quoter)

        
nx.draw(H,pos=nx.spring_layout(H))


NumOfCliqes=nx.graph_clique_number(H)
print ("Clique number of the graph : ")
print (NumOfCliqes)

#
MaxCliques = nx.find_cliques(H)
print ("All maximal cliques: ")
print(list(MaxCliques))
##
#print ("Maximal clique graph")
#cliq=nx.make_max_clique_graph(H)
#nx.draw(cliq,pos=nx.spring_layout(cliq))

node_clique_number=nx.node_clique_number(H)
print ("Size of the largest maximal clique containing each given node")
print (node_clique_number)

number_of_cliques=nx.number_of_cliques(H)
print ("Number of maximal cliques for each node.")
print (number_of_cliques)