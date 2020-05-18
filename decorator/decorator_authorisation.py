from functools import wraps
user_login={"indhu":"hello",
             "karthi":"hello1",
             "sarvesh":"hihi"}

def authorised(func):
    @wraps(func)
    def wrapper(username,password):
        if username in user_login.keys():
            if password in user_login[username]:
                return func(username,password)
        return "Not Authorised"
        
    return wrapper


@authorised
def blog(username,password):
    return "blogs"

@authorised
def content(username,password):
    return "contents"


print (blog('indhu','hello1'))
print (content('indhu','hello'))

print (blog.__name__)





