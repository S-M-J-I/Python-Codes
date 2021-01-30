# Performance Decorator - for testing (to measure how the time taken by a function)
from time import time


def performance(func):
    def wrap_func(*args, **kwargs):
        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        print(f"It took {time_end - time_start} ms")
        return result

    return wrap_func


@performance
def long_time():
    for i in range(10000000):
        var = i * 5
