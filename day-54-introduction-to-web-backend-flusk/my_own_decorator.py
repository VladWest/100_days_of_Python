import time


current_time = time.time()


def speed_calc_decorator(function):
    def wrapped_function():
        function
        end_time = time.time()
        difference = end_time - current_time
        print(f"The time difference is: {difference}")
    return wrapped_function


def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


decorated_func = speed_calc_decorator(fast_function)
decorated_func()

slow_function()
