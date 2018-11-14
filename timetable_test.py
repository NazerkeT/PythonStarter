import json

fname='data.json'
data=open(fname).read()
js=json.loads(data)

print(json.dumps(js))
