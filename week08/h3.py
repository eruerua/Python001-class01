from functools import wraps
import time
def timer(func):
    @wraps(func)
    def wrapped_function(*args,**kwargs):
        time_start = time.time()
        r = func(*args,**kwargs)
        time_stop = time.time()
        print(f'函数{func.__name__}运行时间为{(time_stop-time_start)*1000}ms')
        return r
    return wrapped_function

@timer
def pr(l):
    r=0
    for i in l:
        r+=i
    print(r)

pr(range(0,10000))

