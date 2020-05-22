name="global name"
def outer_fn():
    global name
    name="enclosing name"
    def inner_fun():
        #nonlocal name
        global name
        name="local name"
        print(name)
    inner_fun()
    print(name)
outer_fn() 
print (name)   
