a = open("omdb/pelis.json", "r",encoding="utf8")
c = "nada"
palBusc = "Title"
noLaEncuentro = True
while c != "" and noLaEncuentro:
    c = a.read(1)
    a.seek(a.tell() + 1)
    p = a.read(len(palBusc))
    print(p)
    if p == palBusc:
        noLaEncuentro = False
        print("encontrada", p, "en la posición", a.tell()-(len(p)), "j")
        j = (a.tell()-(len(p)))+8
c = "nada"
comaBusc = ","
noLaEncuentro = True
while c != "" and noLaEncuentro:
    c = a.read(1)
    a.seek(a.tell()-(len(p)))
    c = a.read(len(comaBusc))
    if c == comaBusc:
        noLaEncuentro = False
        print("encontrada", c, "en la posición", a.tell()-(len(c)),"k")
        k =(a.tell()-(len(c)))
a.seek(j)
nombre = a.read(j-k)
print ("NOMBRE",nombre)
