import json
from future.utils import iteritems

dict = {'A':['B','C'],
        'B':['D','E']}

js = json.dumps(dict)
print(dict['A'])
f = open("dict.json","w")
f.write(js)
f.close()
