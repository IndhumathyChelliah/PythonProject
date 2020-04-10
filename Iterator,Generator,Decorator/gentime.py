import random,timeit

l=['a','b','c','d']

print ("Generator time is " ,timeit.timeit("'-'.join(i.upper() for i in l)",setup="from__main__import l"))

l1="-".join([j.upper() for j in l])