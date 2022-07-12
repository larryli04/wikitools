import networkx as nx
import matplotlib.pyplot as plt
import json
import copy
import time
import igraph
from collections import Counter
# Defining a Class

def capitalize(word):
    w = word.rstrip().lstrip()
    try:
        return w[0].upper() + w[1:]
    except:
        print(word=="")
        print(len(word))
        # exit()


graph = igraph.Graph()



def addEdge(g, a, b):
    if(a not in vertices):
        g.add_vertices(a)
        vertices[a] = None
    if(b not in vertices):        
        g.add_vertices(b)
        vertices[b] = None
    
    g.add_edge(a, b)
    
    return g


start = time.time()
with open('wikilinks.json') as json_file:
    data = json.load(json_file)

data = json.loads(data)
end = time.time()
print(f"dictionary has {len(data)} keys")
print(f"Data loaded in {end-start} seconds")

start = time.time()
# only select nodes with > 50 entry points
value_dict = {}
value_dict_count = {}
newdata = {}
for key in data:
    value = data[key]
    k = copy.deepcopy(key)
    if("_" in key or "List of" in key or "#" in key or "WP:" in key):
        continue
    if(value==None or value.lstrip() == "" or len(value)==0):
        continue
    value = capitalize(value)
    
    if value not in value_dict:
        value_dict[value] = 1
        value_dict_count[value] = 1
    elif (value_dict[value] > 0 and value_dict_count[value] < 10):
        newdata[capitalize(key)] = value
        value_dict_count[value] += 1
        # print(value)
    else:
        value_dict[value] += 1

end = time.time()
print(f"Cut down graph in {end-start} seconds")
print(f"dictionary has {len(newdata)} keys")

# start = time.time()
# for key in newdata:
#     graph = addEdge(graph, key, newdata[key])
# end = time.time()

# print(f"graph edges added in {end-start} seconds")

# 16078592
start = time.time()
i=0
sstart = 0
chunk=[]
vertices = {}
for key in newdata:
    value = newdata[key]
    # k = copy.deepcopy(key)
    # if("_" in key or "List of" in key or "#" in key or "WP:" in key):
    #     continue
    # if(value==None or k.lstrip() == "") or len(k)==0:
    #     continue
    if value == None:
        continue
    
    chunk.append((key, value))
    if(key not in vertices):
        vertices[key] = None
    if(value not in vertices):
        vertices[value] = None

    i+=1


    if (i%1000000==0):
        
        print(i, time.time()-sstart)
        sstart = time.time()



graph.add_vertices([t for t in vertices])
graph.add_edges(chunk)
chunk = []
vertices = {}

end = time.time()
print(f"Number of vertices:{graph.vcount()}")
print(f"Number of edges: {graph.ecount()}")
print(f"graph edges added in {end-start} seconds")

start = time.time()
# igraph.plot(graph,layout="auto")
graph.write_graphml("save.graphml")
end = time.time()

print(f"Graph created in {end-start} seconds")

