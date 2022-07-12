import networkx as nx
import matplotlib.pyplot as plt
import json
import copy
import time
import igraph
import random
# Defining a Class

def capitalize(word):
    w = word.rstrip().lstrip()
    try:
        return w[0].upper() + w[1:]
    except:
        print(word=="")
        print(len(word))
        # exit()


graph = igraph.Graph(directed=True)



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
i=0
sstart = 0
fl = "AccessibleComputing"
article = data[fl]

while(i<10000):
    # start at beginning
    fl = capitalize(fl)
    article = capitalize(article)
    
    # if("disambiguation" in fl or "_" in fl or "List of" in fl or "#" in fl or "WP:" in fl or fl==None or fl.lstrip() == "" or len(fl)==0):
    #     continue
    # if("disambiguation" in article or "_" in article or "List of" in article or "#" in article or "WP:" in article or article==None or article.lstrip() == "" or len(article)==0):
    #     continue
    # try:
    #     capitalize(fl)
    #     capitalize(article)
    #     data[capitalize(article)]
    #     data[capitalize(data[article])]
    # except:
    #     continue

    newdata[fl] = capitalize(data[fl]) # set f1 to whatever it links to

    # find next
    try:
        fl = capitalize(data[fl])
        article = capitalize(data[article])
        # print(fl, article)
        # print(data[capitalize(article)])

        if(article in newdata):
            newdata[fl] = article
        while(article in newdata):
            # print(True)
            fl = capitalize(random.choice(list(data.keys())))
            article = capitalize(data[fl])
    except: # article is bad (not processable)
        # print(fl, article)
        fl = capitalize(random.choice(list(data.keys())))
        article = capitalize(data[fl])
    
    i+=1

    if (i%100==0):
        # print(newdata)
        print(i, time.time()-sstart)
        sstart = time.time()
        # go to random
    # add to newdata


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
    value = data[key]
    k = copy.deepcopy(key)
    if("_" in key or "List of" in key or "#" in key or "WP:" in key):
        continue
    if(value==None or value.lstrip() == "" or len(value)==0):
        continue

    value = capitalize(value)
    if value == None:
        continue
    
    chunk.append((key, value))
    if(key not in vertices):
        vertices[key] = None
    if(value not in vertices):
        vertices[value] = None

    i+=1


    if (i%1000==0):
        
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
graph.degree(mode="in")
graph.write_graphml("save_10000.graphml")
end = time.time()

print(f"Graph created in {end-start} seconds")

