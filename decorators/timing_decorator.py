import logging
from functools import wraps
import time

logging.basicConfig(level=logging.INFO)

def note_timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        logging.info(f"Function {func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

# Example usage:
@note_timing
def slow_function():
    time.sleep(2)

slow_function()