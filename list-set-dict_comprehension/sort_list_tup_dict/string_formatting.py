person={'name':'karthi','age':7}

print ("My name is " + person['name'] + ' and I am '+ str(person['age']) + ' years old')
print("My name is {} and I am {} years old".format(person['name'],person['age']))
print (f"My name is {person['name']} and I am {person['age']} years old")

print("My name is {0} and I am {1} years old. Name: {0}".format(person['name'],person['age']))
print("My name is {0[name]} and I am {0[age]} years old".format(person))
print ("My name is {name} and I am {age} years old".format(**person))

l=['indhu',25]
print ("My name is {0[0]} and age is {0[1]}".format(l))

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

print ("My name is {0.name} and age is {0.age}".format(e1))
print ('My name is {name} and age is {age}'.format(name="indhu",age=25))

#formatting zero padded in integers
for i in range(10):
    print ("The number is {:02}".format(i))

# formatting to 2 decimal places
pi=3.1456899
print("pi value is {:.2f}".format(pi))  

#formatting comma seperated integers

print("1 mb equals {:,}".format(1000**2))  

# printing date

import datetime
my_date=datetime.datetime.now()
print(my_date)

print ("Date is {:%B %d,%Y}".format(my_date))


