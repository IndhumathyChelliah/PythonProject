
color=["red","blue","green"]

for i in range(len(color)):
	print (i,color[i])


for i in enumerate(color):
	print (i)

for i,j in enumerate(color):
	print (i,j)


for i,j in enumerate(color,start=1):
	print (i,j)

