# Decorator
def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You are using {fn.__name__} function")
        result = fn(args[0], args[1], args[2])
        print(f"The result is : {result}")
    return wrapper


# Function which need to be decorated
@logging_decorator
def mul(a1, a2, a3):
    return a1 * a2 * a3


mul(2,2,2)
