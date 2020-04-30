
import timeit
str1="-".join(str(n) for n in range(100))
print (str1)
s=timeit.timeit('"-".join(str(n) for n in range(100))',number=100)
print (s)
#using list comprehension
s1=timeit.timeit('"-".join([str(n) for n in range(100)])',number=100)
print (s1)
#using map function
s3=timeit.timeit('"-".join(map(str,range(100)))',number=100)
print (s3)

%timeit='"-".join(str(n) for n in range(100))'
