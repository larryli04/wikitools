import json
import time

def printPath(list):
    out = ""
    for i in range(len(list)-1):
        out += list[i] + "->"
    
    out += list[-1]
    return out

def capitalize(word):
    w = word.rstrip().lstrip()
    return w[0].upper() + w[1:]

start = time.time()
with open('wikilinks.json') as json_file:
    data = json.load(json_file)

data = json.loads(data)
end = time.time()

print(f"Data loaded in {end-start} seconds")



# get random wikipedia article
# for now just use manual input
current = input()
start = time.time()
path = [current]
path.append(capitalize(data[current]))
while(capitalize(data[current]) != "Philosophy"):
    current = capitalize(data[current])
    path.append(capitalize(data[current]))
    print(printPath(path))
print(printPath(path))

# output = capitalize(data[current])
# print(capitalize(output))
while(True):
    win = input()
    print(capitalize(data[win]))


end = time.time()
print(f"Accessed data in {end-start} seconds")
# print(printPath(path))