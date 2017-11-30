import functools

def two_times(func):
    @functools.wraps(func)
    def wrapper():
        print('first time')
        func()
        print('2nd time')
        func()

    return wrapper()