import itertools
print(dir(itertools))

l = [1,2,3]

print(list(itertools.combinations(l,2)))
print(list(itertools.accumulate(l)))

