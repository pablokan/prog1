from copy import copy, deepcopy
ll = [[1, 2], [3, 4]]
ll2 = copy(ll)
ll3 = deepcopy(ll)
ll[0][0] = 100

print(ll)
print(ll2)
print(ll3)

print()

a = [1, 2]
b = a
c = a[:]
a[0] = 10

print(b)
print(c)

