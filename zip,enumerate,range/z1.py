a=("indhu","karthi","sarvesh")

b=("google","Microsoft","apple")

zipped= zip(a,b)

print (zipped)

zip3= list(zipped)

print (zip3)



zip1=set(zip(a,b))
print (set(zip1))
zip2= dict(zip(a,b))
print (zip2)


for i in zip3:
	print (i)

for i in zip1:
	print (i)

for (i,j) in zip2.items():
	print (i,j)



