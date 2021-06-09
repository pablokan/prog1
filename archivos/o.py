f = open('t01.txt', 'r')
t = f.readlines()
print(t)
w = list(map(lambda x: x[:-1], t))
print(w)


