from random import randint

c = 0
n = []
while c < 4:
    z = randint(0, 9)
    if str(z) not in n:
        n.append(str(z))
        c += 1
if n[0] == '0':
    x = randint(1, 3)
    n[0], n[x] = n[x], n[0]
print(n)
