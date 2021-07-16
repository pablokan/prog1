a = '1 2 3 4'.split(' ')
b = '9 2 4 0'.split(' ')

print(set(a).intersection(b))
print(all(i == j for i, j in zip(a, b))   )

