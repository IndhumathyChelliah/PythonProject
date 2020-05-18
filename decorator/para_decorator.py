
from functools import wraps
def prettify(symbol):
    def decorator(func):
        @wraps(func)
        def wrapper(name):
            print(symbol*len(name))
            func(name)
            print(symbol*len(name))
        return wrapper    

    return decorator   


@prettify('-')
def print_name(name):
    print(name)

@prettify('*')
def print_city(city):
    print(city)

print_name("karthi")
print_city("chennai")

print(print_name.__name__)

