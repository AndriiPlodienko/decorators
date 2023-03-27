# decorators

First task:
In this decorator, we use the time library to measure the time of function execution and display the result

Second task:
In this decorator, the wrapper function wrapper takes an arbitrary number of arguments using *args. If the args tuple already exists in the cache dictionary cache_dict, then we have already executed a function with these arguments and can return the stored result. If args has not yet been used, we execute the original func function with these arguments, save the result to the cache_dict cache dictionary using the args key, and return the result.
