from random import randint
c = 0
n = []
while c < 4:
    z = randint(0, 9)
    if str(z) not in n:
        n.append(str(z))
        c += 1

win = False
while not win:
    bien = 0
    regular = 0
    a = input('Número: ')
    for x in range(4):
        for y in range(4):
            if a[x] == n[y]:
                if x == y:
                    bien += 1
                else:
                    regular += 1
    if bien == 4:
        win = True
    else:
        print(bien, "bien y", regular, "regular")

if win:
    print('Acertó!', n)
    


