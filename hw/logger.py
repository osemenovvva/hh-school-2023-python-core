import functools
import time

def logger_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_date = time.time()
        print(f'Start of function {func.__name__} execution')
        result = func(*args, **kwargs)
        end_date = time.time()
        print(f'End of function {func.__name__} execution')
        print(f'Execution time: {end_date - start_date}')
        return result

    return wrapper