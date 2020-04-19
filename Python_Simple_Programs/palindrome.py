l1=[123,456,789,333,222,111,343,545]
pal_list=[]

rev=0

for a in l1:
  while a>0:
    rev=rev*10+a%10
    a=a//10
  if a==rev:
    pal_list.append("palindrome")
  else:
    pal_list.append("not palindrome")
    
print (pal_list)

