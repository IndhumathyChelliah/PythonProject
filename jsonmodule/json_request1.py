import json
import requests
request=requests.get("https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_key=kj_7cGVgb4WhBxs92uz4")
request_text=request.text
data=json.loads(request_text)

print (type(data))

data_serialized=json.dump(data,open("data.json","w"),indent=4)
