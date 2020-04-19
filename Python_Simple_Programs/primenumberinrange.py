n=[a for a in range(1,51)]

primeno=[]

for i in n:
 b=i
 count=0
 for c in range(1,b):
   if b%c==0:
     count=count+1
 if count<2:
   primeno.append(b)
print (primeno)


