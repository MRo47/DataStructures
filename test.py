import json
from future.utils import viewitems

nodes = {'A':['B','C'],
         'B':['D','E']}

js = json.dumps(nodes)
print(nodes['A'])
f = open("dict.json","w")
f.write(js)
f.close()

for (key, value) in viewitems(nodes):
    print(key, value)

for key in nodes:
    for value in nodes[key]:
        print(value)
