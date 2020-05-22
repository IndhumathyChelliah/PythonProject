#sorting list 

l1=[1,2,3,6,5,4,9,8,7]

#sorted will return another sorted list
l2=sorted(l1)
print(l2)

#sort in descending order
l3=sorted(l1,reverse=True)
print(l3)

#l1.sort() -> will sort l1 list itself. it will retrun None.
#this method works only in list. whereas sorted fn works in tuple,dict
print (l1.sort())
# below is correct one
l1.sort()
print(l1)

#sorting tuples
s1=(1,2,4,5,6,7,2,9,8)
s2=sorted(s1)
print(s2)

#sorting dictionary

d1={"name":"indhu","age":25,"city":"chennai"}
#sorted -> by defualt sort the keys and return keys alone
d2=sorted(d1)
print(d2)

#sorting list based on absolute values

li=[-1,-2,3,4]
li2=sorted(li,key=abs)
print(li2)

#sorting objects

class Employee:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def __repr__(self):
        return "'{}'-{}-'{}'".format(self.name,self.age,self.city)

e1=Employee("indhu",25,"chennai")
e2=Employee("karthi",7,"nellai")   
e3=Employee("Sarvesh",3,"karur")

e=[e1,e2,e3]     
#method 1
from operator import attrgetter
sort_e=sorted(e,key=attrgetter('age'))
print(sort_e)

#method 2
sort_e1=sorted(e,key=lambda e:e.age)
print(sort_e1)

#method 3

def e_sort(emp):
    return emp.age

sort_e2=sorted(e,key=e_sort,reverse=True)
print(sort_e2)    


