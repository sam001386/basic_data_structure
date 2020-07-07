'''
Reference: 
https://www.youtube.com/watch?v=5VCywjS8YEA&t=767s
'''
# Simple application of decorator
import time
def timeit(func):
    def inner():
        s = time.time()
        func()
        e = time.time()
        print(f'{func.__name__} finished in {e - s} seconds.')
    return inner
        
@timeit
def slow_method():
    time.sleep(2.5)
    print("Done!")
    
slow_method()

###### Fibonacci ########3

class Mycache(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        if not args in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Mycache
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)  

print(fib(400))
