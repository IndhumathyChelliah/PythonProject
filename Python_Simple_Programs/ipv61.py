import re

ip1=input("Enter IPV6 Address: ")

pattern=re.compile(r"^([0-9A-Fa-f]{1,4})\:([0-9A-Fa-f]{1,4})\:([0-9A-Fa-f]{1,4})\:([0-9A-Fa-f]{1,4})\:([0-9A-Fa-f]{1,4})\:([0-9A-Fa-f]{1,4})\:([0-9A-Fa-f]{1,4})\:([0-9A-Fa-f]{1,4})$")

i1=re.search(pattern,ip1)

if (i1):
 print ("Valid IP v6 address")
else:
 print ("Invalid IPv6 address")