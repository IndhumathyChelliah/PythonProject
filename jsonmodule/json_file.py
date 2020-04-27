import json

with open ("new_states.json","r") as f:
	data=json.load(f)

for state in data["states"]:
	print (state)

for state in data["states"]:
	print (state["name"],state["abbreviation"])

for state in data["states"]:
	del state["abbreviation"]

with open("states.json","w")as f1:
	new_string=json.dump(data,f1,indent=2)

