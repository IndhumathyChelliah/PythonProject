
s1={1,2,3}
s2={2,3,4}
s3={3,4,5}

#intersection
s4=s1.intersection(s2)
print (s4)
s5=s1.intersection(s2,s3)
print (s5)

#union
s6=s1.union(s2)
print (s6)
s7=s1.union(s2,s3)
print (s7)

#difference
s8=s1.difference(s2)
print (s8)
s9=s1.difference(s2,s3)
print (s9)

#symmetric_difference
s10=s1.symmetric_difference(s2)
print (s10)


