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

win = False
intentos = 0
while not win:
    bien = 0
    regular = 0
    a = input("Número: ")
    intentos += 1
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
        print(f"{bien} bien y {regular} regular. Intento #{intentos}")

if win:
    print(f"Acertó! Número: {''.join(n)}. Intentos: {intentos}", )
