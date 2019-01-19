##create graph
import json
import networkx as nx
import couchdb


def BuildGraph(jsonIN):

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

couchServer = couchdb.Server("http://localhost:5984")
idtable=[]
dbname = 'scientists'
db = couchServer[dbname]

for docid in db.view('_all_docs'):
    
    i = docid['id']
    jsonOUT = db[i]
    print(jsonOUT)
    BuildGraph(jsonOUT)
    

nx.draw(G,pos=nx.spring_layout(G))


MaxCliques = nx.find_cliques(G)
print ("Maksymalne kliki to: ")
print(list(MaxCliques))

print ("Maksymalna klika")
cliq=nx.make_max_clique_graph(G)
nx.draw(cliq,pos=nx.spring_layout(cliq))
# 
print ("Dwudzielny wykres klikowy?")
bipart=nx.make_clique_bipartite(G)
nx.draw(bipart,pos=nx.spring_layout(bipart)) 

NumOfCliqes=nx.graph_clique_number(G)
print ("Liczba klik")
print (NumOfCliqes)

MaxNumOfCliqes=nx.graph_number_of_cliques(G)
print ("Liczba maksymalnych klik")
print (MaxNumOfCliqes)

node_clique_number=nx.node_clique_number(G)
print ("node_clique_number")
print (node_clique_number)

number_of_cliques=nx.number_of_cliques(G)
print ("number of maximal cliques for each node.")
print (number_of_cliques)
