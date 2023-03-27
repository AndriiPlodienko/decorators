import time

class TimingDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {self.func.__name__} took {end_time - start_time} sec.")
        return result
    
@TimingDecorator
def my_function():
    time.sleep(2)

my_function()