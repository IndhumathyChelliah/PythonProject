import re

ip=input("Enter ip address: ")

pattern=re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}$")

m1=re.search(pattern,ip)

if (m1):
  print ("valid ip address")

else:
 print ("invalid ip address")





