import sys
infinite = 1e309
print(infinite, type(infinite))
maxInt = sys.maxsize

if -infinite < maxInt < infinite:
    print(maxInt)

