
a,b=0,1
for i in range(10):
    print (a)
    a,b=b,a+b

#Fib- Generator
def fib(num):
    a,b=0,1
    for i in range(10):
        yield a
        a,b=b,a+b

for item in fib(10):
    print (item)

