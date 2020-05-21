
from dataclasses import dataclass,field,asdict

@dataclass(order=True)
class Employee:
    first:str=field(compare=False)
    last:str=field(compare=False)
    pay:int
    fullname:str=field(init=False,repr=False,compare=False)
    email:str=field(init=False,repr=False,compare=False)

    def __post_init__(self):
        
        self.fullname=self.first+self.last 
        self.email=self.first+"." +self.last+"@company.com"    
  


e1=Employee("indhu","mathy",500)
e2=Employee("karthi","palani",1000)   
print (e1)
print(e1>e2) 
print (e1==e2) 
print (e1.fullname)
print (e1.email)
emp_dict=e1.__dict__
print(emp_dict)
print (asdict(e1))
# converting object to json
import json
jdata=json.dumps(emp_dict,indent=2)
print (jdata)





            


