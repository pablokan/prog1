from calcula_edad import edad

nom = open('nombres.txt', 'r')
fec = open('fechas.txt', 'r')
n = nom.readlines()
f = fec.readlines()

for x in range(len(n)):
    if edad(f[x]) >= 18:
        print(n[x], 'Es mayor de edad.')