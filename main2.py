def cache(func):
    cache_dict = {}
    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = func(*args)
            cache_dict[args] = result
            return result
    return wrapper

@cache
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(7)) # done counting
print(factorial(7)) # return from cache without counting
