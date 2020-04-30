
from collections import Counter

l=[1,2,3,4,2,3,4,5,62,3,1]
print (Counter(l))

s="aaddssff"
print (Counter(s))

words="hello how are you hi how are you"
word=words.split()
c=(Counter(word))
print (c.most_common(2))
#total of all counts
print (sum(c.values()))

#list unique elements
print (list(c))

#convert to set
print (set(c))

#convert to dict
print (dict(c))

#convert to a list of (element,cnt)pairs
print (c.items())



