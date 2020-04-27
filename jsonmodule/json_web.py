import json
from urllib.request import urlopen
with urlopen("https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_key=kj_7cGVgb4WhBxs92uz4") as response:
	source=response.read()


data=json.loads(source)

print (type(data))

#data_serialized=json.dump(data,open("data.json","w"),indent=4)
print (len(data["dataset"]["column_names"]))

for item in data["dataset"]["data"]:
	print (item[2])