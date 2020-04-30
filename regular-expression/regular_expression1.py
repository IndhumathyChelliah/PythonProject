import re

string="sHello hello how are you"

pattern=re.compile(r'[H]\w*',re.I)

matches=pattern.finditer(string)

for m in matches:
    print (m)
# retuns all match items in the list
match=pattern.findall(string)
print (match)

# matches only starting of string
match1=pattern.match(string)
print (match1) 
# returns only first matched object
match2=pattern.search(string)
print (match2)   







