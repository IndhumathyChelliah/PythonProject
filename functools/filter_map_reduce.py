from functools import reduce


# to find even mumber

l=[1,2,3,4,5,6,7,8,9,10]

evens=list(filter(lambda x : x%2==0 ,l))

print (evens)

# Return the square of all numbers in the list

square=list(map(lambda x: x*2 ,l))

print (square)

#to find the sum of all numbers in the list using reduce

sum=reduce(lambda a,b: a+b ,l)
print (sum)

# find the biggest number in the list

l1=[2,3,6,4,65,43,23]

bigno=reduce(lambda x1,x2:x1 if (x1>x2)  else x2, l1)
print (bigno)

bigno2=reduce(lambda x,y: max(x,y),l1)

print (bigno2)