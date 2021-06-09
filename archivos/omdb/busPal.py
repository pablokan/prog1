a = open("omdb/palabras.txt", "r")

c = "nada"
palBusc = "jota"
noLaEncuentro = True

while c != "" and noLaEncuentro:
    c = a.read(1)
    if c == "-":
        a.seek(a.tell() + 1)
        p = a.read(len(palBusc))
        if p == palBusc:
            noLaEncuentro = False
            print("encontrada", p, "en la posición", a.tell()-len(p))

if c=="" and noLaEncuentro:
    print("no ta")

a.close()

    