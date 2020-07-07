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
