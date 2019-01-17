##create graph
import json
import networkx as nx

json1 = {
  "author": "Max Planck",
  "quotingperson":"Albert Einstein"
}
json2= {
    "author":("Albert Einstein", "Niels Bohr"),
    "quotingperson": ("Pierre Curie", "Hendrik Lorentz")
    }
json3= {
    "author":("Pierre Curie", "Niels Bohr"),
    "quotingperson": ("Max Planck", "Hendrik Lorentz", "Albert Einstein")
    }
# convert into JSON:
convert1 = json.dumps(json1)
convert2 = json.dumps(json2)
convert3 = json.dumps(json3)

# the result is a JSON string:
 
toBuild1 = json.loads(convert1)
toBuild2 = json.loads(convert2)
toBuild3 = json.loads(convert3)

def BuildGraph(jsonloads):

    if type(jsonloads["author"]) == list:   #add author nodes, several authors
        G.add_nodes_from(jsonloads["author"])
    elif type(jsonloads["author"]) == str:  #add author nodes, one author
        G.add_node(jsonloads["author"])
    else:
        print ("")

    if type(jsonloads["quotingperson"]) == list:         ##add quoting nodes, several citations
        G.add_nodes_from(jsonloads["quotingperson"])
        
    elif type(jsonloads["quotingperson"]) == str:       #add quoting node, one citation
        G.add_node(jsonloads["quotingperson"])
    else:
        print ("")
        
        
        
    if type(jsonloads["author"]) == list:   #draw edges
        
        if type(jsonloads["quotingperson"]) == str:             #several authors, one citation
            for x in jsonloads["author"]:
                G.add_edges_from([(x, jsonloads["quotingperson"])])
        
        elif type(jsonloads["quotingperson"]) == list:          #several authors, several citations
           for x in jsonloads["quotingperson"]:
               for y in jsonloads["author"]:
                   G.add_edge(y, x)
        
        
    elif type(jsonloads["author"]) == str:
        
        if type(jsonloads["quotingperson"]) == str:             #one author, one citation
            G.add_edges_from([(jsonloads["author"], jsonloads["quotingperson"])])
        
        elif type(jsonloads["quotingperson"]) == list:          #one author, several citation
            for x in jsonloads["quotingperson"]:
                G.add_edges_from([(jsonloads["author"], x)])
                
    
    
G = nx.Graph()


BuildGraph (toBuild1)
BuildGraph (toBuild2)
BuildGraph (toBuild3)

print ("Graf")
nx.draw(G,pos=nx.spring_layout(G))

MaxCliques = nx.find_cliques(G)
print ("Maksymalne kliki to: ")
print(list(MaxCliques))

print ("Maksymalna klika")
cliq=nx.make_max_clique_graph(G)
nx.draw(cliq,pos=nx.spring_layout(cliq))
 
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

