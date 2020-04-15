
l1=[2,3,4,5,6,5,4,3]
# by changing list to set and then converting to list
s1=set(l1)

l2=list(s1)

print (l2)

# define function to remove duplicates
l2=[]

for i in l1:
	if i not in l2:
		l2.append(i)
print (l2)		