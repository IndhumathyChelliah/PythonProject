
import itertools
letters=['a','b','c']
numbers=[1,2]
names=['karthi','sarvesh']

#this method takes more space in memory for large list
#combined =letetrs+numbers+names

combined=itertools.chain(letters,numbers,names)

for item in combined:
	print (item)

#islice

result=itertools.islice(range(10),1,5,2)
for item in result:
	print (item)

#example for islice

with open("sample.txt","r") as f:
	header=itertools.islice(f,3)

	for line in header:
		print (line, end="")

#itertools.compress(similar to filter fn -> filter we will give fn to determin True or False.)
selectors=[True,False,True]
result1=itertools.compress(letters,selectors)
print(list(result1))

#filter
even=filter(lambda x: x%2==0,range(10) )
print (list(even))

#itertools.filterfalse:
odd=itertools.filterfalse(lambda x: x%2==0,range(10) )
print (list(odd))

def lt_2(n):
	if n<2:
		return True
	return False
l1=[1,2,3,1,2,3]
result2=itertools.dropwhile(lt_2,l1)
print (list(result2))

result3=itertools.takewhile(lt_2,l1)
print (list(result3))








