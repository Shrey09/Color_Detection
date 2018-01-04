import json

json_data = open('dataset.js')
data=json.load(json_data)
for i in data:
	print("%d, %d, %d, %s"%(i['x'],i['z'],i['y'],i['label']))
