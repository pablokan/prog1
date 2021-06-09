a = open("omdb/num.txt", "r")

posi = 0
c = "nada"
n = "cuatro"
noLoEncuentro = True

while noLoEncuentro and c != "":
    c = a.read(1)
    if c == "-":
        posN = a.seek(a.tell()+1)
        num = a.read(len(n))
        print(num)
        if num == n:
            noLoEncuentro = False
        else:
            c = a.read(1)

print("Número", n, "encontrado en posición", a.tell())


a.close()



