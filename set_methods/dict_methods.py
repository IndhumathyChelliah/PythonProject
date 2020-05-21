d={'name':'karthi',
   'age':7,
   'city':'chennai',
    }
#will print only the keys
for i in d:
    print (i)
#will print the (key,value) as a tuple   
for i in d.items():
    print (i)
#will print the key,value in the format specified
for i,j in d.items():
    print(i,j)

#will print only the keys    
for i in d.keys():
    print(i)
#will print only the values    
for i in d.values():
    print(i)

#get(accessing like index)

print(d.get("name"))

#fromkeys()
#The fromkeys() method returns a dictionary with the specified keys and the specified value.
a={'a','e','i','o','u'}
b='vowels'
d1=dict.fromkeys(a,b)
print(d1)

#setdefault - if key is not there , will add the key with value none
person = {'name': 'indhu', 'age': 22}
city = person.setdefault('city')
print(person)
#setdefault- if key  is not  there , will add key and value specified
person = {'name': 'indhu', 'age': 22}
city = person.setdefault('city','chennai')
print(person)

#setdefault-> if key is present, returns the value of that specified key
person = {'name': 'indhu', 'age': 22}
#age=person.setdefault('age',25)
print(person.setdefault('age',25))

#update- combining - merging bith dictionaries and updated d1
print(d1.update(d))
print(d1)

#popitem
#The popitem() method removes and returns the last element (key, value) pair inserted into the dictionary.
print(d1.popitem())
print(d1)

#pop
#The pop() method removes and returns an element from a dictionary having the given key.
print (d1.pop('a'))
print(d1)

#clear
d1.clear()
print (d1)

#copy
d1=d.copy()
print (d1)
import copy
d2=copy.deepcopy(d1)
print (d2)





