s1={1,2,3}
#add
s1.add(4)
print (s1)
#clear
s1.clear()
print(s1)
#copy
s1={1,2,3}
s2=s1.copy()
print(s2)
#difference
s3={1,2,3,4,5,6}
s5=s3.difference(s1)
print(s5)
#union
s6=s1.union(s3)
print(s6)
#intersection
s7=s3.intersection(s5)
print (s7)
#isdisjoint
print (s3.isdisjoint(s1))
#issubset
print(s3.issubset(s1))
#issuperset
print(s3.issuperset(s1))
#pop-> will delete the first element in the set
print(s3.pop())
print (s3)
#setdiscard- remove the element mentioned. if element is not present, will not throw error
print (s3.discard(2))
print (s3)

