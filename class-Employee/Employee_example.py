class Employee:
    emp_count=0
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        Employee.emp_count+=1
    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    @fullname.setter 
    def fullname(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last=last


    @property
    def email(self):
        return "{}.{}@company.com".format(self.first,self.last)

    @classmethod    
    def set_raiseamt(cls,amount):
        cls.raise_amount=amount

    @classmethod
    def from_dict(cls,data):
        emps=[]
        for emp in data:
            new_emp1=cls(emp['first'],emp['last'],emp['pay'])
            emps.append(new_emp1)
        return emps

    @classmethod
    def from_string(cls,string1):
        first,last,pay=string1.split("-")
        return cls(first,last,pay)

    def applyraise(self):
        self.pay=self.pay*self.raise_amount
        return self.pay

        

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __str__(self):
        return "{}-{}-{}".format(self.first,self.last,self.pay)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

    @staticmethod
    def is_eligible(age):
        if age>=18:
            print ("Eligible to be an Employee")
        else:
            print ("Sorry Not Eligible")
            



e2=Employee("Sarvesh","Palani",400)
print (e2.fullname)
print (e2.email)
print (e2.emp_count)
print (e2)
# object representation ny repr() method
print (repr(e2))

#object representation in dictionary form
print (e2.__dict__)
#setting class variable by using classmethod
Employee.set_raiseamt(1.08)
e2.applyraise()
print (e2.pay)

#setting fullname
e2.fullname="Sarvesh Palanichamy"
print(e2)

e3=Employee("Palani","rama",1000)
#operator Overloading done by special methods (__add__)
print (e2+e3)
print (len(e2))

#static method:(accessed using class and also by instances)
e2.is_eligible(19)
Employee.is_eligible(17)

#sorting employee object
employees=[e2,e3]
#method 1
from operator import attrgetter
new_emplist=sorted(employees,key=attrgetter('pay'))
print (new_emplist)

#method2
new_emplist1=sorted(employees,key=lambda e: e.pay)
print (new_emplist1)



# converting string to object
string1="karthi-palani-250"
e1=Employee.from_string(string1)
print (e1.fullname)
print (e1.email)
print (Employee.emp_count)

#converting list of dictiory to list of objects
data=[{'first':'indhu',
       'last':'mathy',
       'pay':250},
       {
       'first':'karthi',
       'last':'palani',
       'pay':500
       }
    
]


a=Employee.from_dict(data)

print (a[1].first)

print (Employee.emp_count)

#converting object to json data
import json
dictdata=e2.__dict__
jstring=json.dumps(dictdata,indent=2)
print (jstring)








