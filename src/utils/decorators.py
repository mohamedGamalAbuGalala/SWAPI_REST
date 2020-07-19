
from functools import wraps
import time


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = f(*args, **kwargs)
        end = time.perf_counter()
        print(f'Finished {f.__name__!r}: {(end-start):.3f} secs')
        return result
    return wrapper
