### Decorators ###
### Decorators are functions that modify other functions' behavior. They're powerful for aspects like logging, timing, access control, and caching.

### Example:
import logging
import functools
import inspect

logging.basicConfig(level=logging.INFO)

def log_function_calls(func):
    # the below decorator is used to preserve the metadata of the original function like name, docstring, etc.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # get parameter names
        arg_names = inspect.signature(func).parameters
        arg_repr = [f"{name}={value}" for name, value in zip(arg_names, args)]
        kwargs_repr = [f"{name}={value}" for name, value in kwargs.items()]
        all_args = ", ".join(arg_repr + kwargs_repr)
        
        logging.info(f"Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned: {result}")
        
        # return the result of the original function
        return result
    return wrapper
    
# Example usage:
@log_function_calls
def add(a, b, c=10):
    return a + b + c

print(add(1, 2))
print(add(1, 2, c=3))