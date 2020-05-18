
# to convert list of dictionary to list of Student objects
class Student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno

    @classmethod
    def fromdict(cls,data):
        students=[]
        for d in data:
            s=cls(d["name"],d["age"],d["rollno"])
            students.append(s)
        return students    

    def __str__(self):
        return "Name:{},Age:{},RollNo:{}".format(self.name,self.age,self.rollno)
        

        


data=[
{
  "name":"indhu",
  "age":35,
  "rollno":12,  
},
{
    "name":"karthi",
    "age":7,
    "rollno":7

}
]        


a=Student.fromdict(data)
print(a)

print(a[1].name)