from collections import namedtuple

cat=namedtuple('cat',"name,age,breed")

c=cat("jammy",2,"pomerian")

print (c.name)
print (c[1])
print (getattr(c,'breed'))