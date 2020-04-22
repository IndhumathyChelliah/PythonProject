from collections import Counter
from collections import ChainMap
from collections import defaultdict
from collections import OrderedDict

#counter

a=[1,2,3,1,2,3,4,5]
b=Counter(a)
print (b)
print (b[1])
#Chainmap

d1={'a':1,'b':2,'c':3}
d2={'c':4,'d':5,'e':6}

d3=ChainMap(d1,d2)
print (d3)
print(d3['c'])

#defailtdic
name="hellopython"

d=defaultdict(int)
for i in name:
	d[i]+=1
print (d)	

#ordereddic

scores=[('indhu',100),('karthi',101),('sarvesh',102)]
print (type(scores))
d={}
for i,j in scores:
	d[i]=j
print (d)

odict=OrderedDict(scores)
print (odict)
print (type(odict))
print (odict.keys())
print (odict.values())








