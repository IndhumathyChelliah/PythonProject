# type hinting will give u a hint about the types of paramaters
def add(a:int,b:int=1)->int:
    return(a+b)

help(add)

print(add(1,1))

#using typing module for list datatye

from typing import List

def add_list(l:List[int]):
    return(sum(l))

help(add_list)

print (add_list([1,2,3]))

#to include two data types, union module is used

from typing import Union
def divide(a:Union[int,float],b:Union[int,float]):
    return a/b
help(divide)

#to support any kind of data type - module Any

from typing import Any

def anything(a:Any):
    print (a)

#when both parameters hv to be same datatype-> Typevar module

from typing import TypeVar

t=TypeVar('t')

def add(a:t,b:t)->t:
    return(a+b)

help(add)    



