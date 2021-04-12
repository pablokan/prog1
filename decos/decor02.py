import time 
import random

def stopwatch(f):
    def func(*args, **kwargs):
        tic = time.time()
        result = f(*args, **kwargs)
        print(f"{f.__name__} demoró: {time.time() - tic}")
        return result 
    return func

@stopwatch
def sleep_random(s):
    t = s + random.random()
    time.sleep(t)
    return f"Done"

print(sleep_random(1))

@stopwatch
def mil():
    for x in range(1000):
        pass

mil()
