# my own decorator function
def my_decorator(func):
    def wrap_func():
        func()
    return wrap_func

