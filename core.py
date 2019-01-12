import os
import time
import random
import networkx as nx

scientistsGraph = nx.MultiDiGraph()

#f = open('scrappedTitles.txt', 'r+')
#f.truncate(0)
#f.close()

#f = open('scrappedAuthors.txt', 'r+')
#f.truncate(0)
#f.close()

print("Scrapping...")

os.system('python scholar.py --citations-only -c 1 --author "cezary zielinski"') # change to list of authors
scientistsGraph.add_node("cezary zielinski")

time.sleep(1 + random.uniform(10, 20))

print("Scrapped articles:")

i = 1
with open('scrappedTitles.txt', 'r') as f:
    for line in f:
        commandLine = ('scholar.py -c 1 --phrase ' + line.rstrip() + ' --citation bt')
        print(commandLine, '\n')
        os.system(commandLine)
        time.sleep(1 + random.uniform(10, 20)) 
        ++i
        if i >= 1:
        	break


with open('scrappedAuthors.txt', 'r') as f:
    for line in f:
        scientistsGraph.add_edge("cezary zielinski", line.rstrip())



#print(nx.find_cliques(scientistsGraph)) #not implemented for multi directed graph








#lines = [line.rstrip('\n') for line in open('filename')]


#For each title run scholar.py with command -> 
    #scholar.py -c 1 --phrase "Robot control system design exemplified by multi-camera visual servoing" --citation bt
    
    #For each result run following code:
        #str = result
        #pattern = r"title={(.*?)}"
        #result = re.findall(pattern, str, flags=0)
        #print(result)
