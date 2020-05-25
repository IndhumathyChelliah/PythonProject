d1={'name':'indhu',
'age':25}
d2={'name':'karthi',
'age':7}
d3={'tech':'Python'}

l1=['python','sql','tableau','django']

def d(*args,**kwargs):
    print (args)
    print(kwargs)

d(*l1,**d2) 

def merge(d1,d2):
    result={**d1,**d2}
    return result
print (merge(d1,d3))

def merge1(d1,d2):
    d1.update(d2)
    return d1
print(merge1(d1,d3))    

