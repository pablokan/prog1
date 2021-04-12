import random
import time
from codetiming import Timer

@Timer(name="decorator")
def sleep_random(s):
    t = s + random.random()
    time.sleep(t)
    return f"Done"

print(sleep_random(1))
