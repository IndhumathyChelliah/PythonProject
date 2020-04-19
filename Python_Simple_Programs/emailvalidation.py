import re

pattern=re.compile(r"([A-Za-z0-9\-_\.]+)@([A-Za-z0-9\-_]+)\.(com|edu|co.in)")

with open("hello.txt") as file:
  f1=file.read()
  print (f1)
  i2=re.findall(pattern,f1)
  print (i2)
  