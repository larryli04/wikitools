from anytree import Node, RenderTree, find
import requests
import random

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

start = input("start:")
target = input("target:")
pllimit = "50"
default = "||"
next = default
PARAMS = {
    "action": "query",
    "format": "json",
    "titles": start,
    "prop": "links",
    "pllimit": pllimit,
    "plcontinue": default
}
child = []
parent = Node(start)

def func(root):
    global next
    print(next)
    if(find(parent, lambda node: node.name == root).depth == 5):
        return
    child = []
    count = 0
    links = []
    test = []
    n=500
    loadNext = True
    next = "||"
    while(loadNext == True):
        PARAMS = {
            "action": "query",
            "format": "json",
            "titles": root,
            "prop": "links",
            "pllimit": pllimit,
            "plcontinue": next

        }
        R = S.get(url=URL, params=PARAMS)

        DATA = R.json()
        try:
            print(DATA["batchcomplete"] == "")
        except:
            print("not yet")

        PAGES = DATA["query"]["pages"]


        for i, j in PAGES.items():
            try:
                for k in j["links"]:
                    if((("Wikipedia:" in k["title"])==False) and (("Help:" in k["title"])==False) and (("Category:" in k["title"])==False) and (("Template:" in k["title"])==False) and (("Talk:" in k["title"])==False) and (("Portal:" in k["title"])==False)):
                        test.append(k["title"])
                        links.append(Node(k["title"]))
            except:
                return
        try:
            next = DATA["continue"]["plcontinue"]
        except:
            print(DATA["batchcomplete"])
            print("SKFHBAEGUB")
            loadNext = False
    #print(test)
    #if(target in test):
        #child.append(Node(target))

    #delete
    if(len(links)<=n):
        print("nope")
        n = len(links)

    while(count<n):
        pick = random.randint(0, len(links)-1)
        #print(pick)
        rand = links[pick]
        #print(rand)
        print(len(child))
        print(rand)
        print(n)
        if((rand in child) == False):
            if(find(parent, lambda node: node.name == rand.name) == None):
                child.append(rand)
                count += 1
            else:
                count+=1
    #delete

    for i in range(0, len(links)):

        if(find(parent, lambda node: node.name == links[i].name) == None):
            child.append(links[i])


    x = find(parent, lambda node: node.name == root)
    x.children = child
    print(RenderTree(parent))
    if(find(parent, lambda node: node.name == target) != None):
        print("yay")
        print(find(parent, lambda node: node.name == target))
        exit()
    for i in range(0, len(child)):

        func(x.children[i].name)



func(start)
print(RenderTree(parent))
