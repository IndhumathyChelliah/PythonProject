
#mypy typechecking1.py
#static type checking - finding typeError even before pgm is executed
from typing import List

def add_list(l:List[int])->int:
    return sum(l)

l=[1,2,3,4]

print (add_list(l))  

l1=["a","b"]

print (add_list(l1))  