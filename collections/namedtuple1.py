
from collections import namedtuple

Color=namedtuple('Color',['red','green','blue'])
c1=Color(55,255,155)
c2=Color(12,13,14)
#attributes of named tuple can be accessed by index number.
#access by index
print (c1[0])
# access by name
print (c2.red)
# access by getattr
print (getattr(c2,'red'))
