
l1=[1,2,3,4,5,6]
#list comprehension
# [ value for loop if condition]
# finding odd nos
l2=[n for n in l1 if n%2==0]
print (l1)
# list of tuples - iterates through two lists
l3=[(i,j) for i in l1 for j in l2]
print (l3)

#set comprehension

l1=[1,2,3,1,2,3,4,1,2]

s1=set(l1)
print (s1)

s2={n*n for n in l1}
print (s2)

#dict comprehension

l1=['color','fruit','vegetable','shapes']
l2=['red','apple','carrot','square']

d1={key:value for key,value in zip(l1,l2)}
print (d1)

d2={key:value for key,value in zip(l1,l2) if value!='square' }
print (d2)

#generator expression-> it will return a generator object - we hv to iterate thorugh that

g1=((key,value) for key,value in zip(l1,l2))
print (g1)
for i in g1:
    print (i)

l1=[1,2,3]
g2=(n*n for n in l1)   
print (g2)

for i in g2:
    print (i)


