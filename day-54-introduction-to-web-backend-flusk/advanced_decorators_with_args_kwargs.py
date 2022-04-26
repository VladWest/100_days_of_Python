## ********Day 55 Start**********

## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    # Added args and kwargs to method options to provide possibility to have access to object created from class
    def wrapper(*args, **kwargs):
        # Here we are checking for state of variable in created object
        # raw also can be replaced by:
        # if user.is_logged_in == True
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)