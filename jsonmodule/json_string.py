
import json

people_string='''
{ "people":[
           {"name":"indhu",
            "email":["indhu@email.com","indhu1@email.com"],
            "has_license":false
             },
            {
            "name":"karthi",
            "email":null,
            "has_license":true
            }
     ]
}
'''

data=json.loads(people_string)
print (data)
print (type(data))

for person in data["people"]:
	print (person["name"])

for person in data["people"]:
	print (person)

new_string=json.dumps(data,indent=2,sort_keys=True)
print (new_string)	

