arc = open("omdb/num.txt", "r")

c = "nada"
num = "uno"
noLoEncuentro = True

while c != "" and noLoEncuentro:
    c = arc.read(1)
    if c == "-":
        arc.seek(arc.tell()+1)
        n = arc.read(len(num))
        if n == num:
            noLoEncuentro = False
            print(n, "encontrado en la posición", arc.tell())

arc.close()
