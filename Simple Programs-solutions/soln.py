
from dataclasses import dataclass,field,asdict

@dataclass
class Address:
    city:str
    state:str
    zip:int

@dataclass
class Developer:
    fname:str
    lname:str
    age:int
    fullname:str=field(init=False)
    address:Address
    skillset:str=field(init=False)
    def __post_init__(self):
        self.fullname=self.fname+" "+self.lname
        self.skillset=['Python','SQL','Tableau','AWS']
        return self.fullname,self.skillset
a=Address("chennai","TN","627117")        
d=Developer("indhu","mathy",25,a)
 
print (d)
dict=asdict(d)
print (dict) 

@dataclass
class dict_process:
    fname:str
    lname:str
    age:int
    fullname:str
    address:str
    skillset:str

def d_process():
    fname=dict['fname']
    lname=dict['lname']
    age=dict['age']
    fullname=dict['fullname']
    address=dict['address']
    skillset=dict['skillset']
    return dict_process(fname,lname,age,fullname,address,skillset) 

s=d_process()
print (s)

print (s.fname )








