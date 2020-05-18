
import pickle
import json
from dataclasses import dataclass,asdict

class Student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno

s=Student("indhu",30,12)

pickle.dump(s,file=open("test.pkl","wb"))

new_s=pickle.load(file=open("test.pkl","rb"))
print (new_s)
print (new_s.name)

@dataclass
class Employee:
    name:str
    age:int
    rollno:int

e=Employee("karthi",25,12)    

s1=json.dumps(asdict(e))

print(s1)

