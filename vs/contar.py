from collections import Counter

l = [1,2,3,2,2,1,2,2,2,2,2]
c = Counter(l)
print(c, type(c))
print(c[1])

m = ["a","b","a","b","b","a","c","a"]
cL = Counter(m)
print(cL)
print(cL['a'])
