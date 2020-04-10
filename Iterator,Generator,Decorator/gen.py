
def myrange():

	yield 5
	yield 6
	yield 7
	yield 8

values=myrange()

print (values)

print (next(values))
print (values.__next__())

for i in values:
	print (i)

#top 10 perfect squares:

def square():
	for x in range(1,11):
		yield x*x
sq=square()
print (sq)

print (next(sq))
print (sq.__next__())
for j in sq:
	print (j)


def square1():
	n=1
	while n<11:
		yield n*n
		n=n+1

sq1=square1()
for k in sq1:
	print (k)


