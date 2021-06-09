p = open("omdb/pelis.json", "r")
c = "nada"
nombres = []
corchete = p.read(1)
while c != "":
    while c != '"':
        c = p.read(1)
    t = p.read(5)
    if t == 'Title':
        ti = ""
        p.seek(p.tell()+4)
        while c != ',':
            c = p.read(1)
            ti += c
        ti = ti[:-2]
    print(ti)
    nombres.append(ti)
    dosPuntos = 0
    while dosPuntos < 8:
        c = p.read(1)
        if c == ":":
            dosPuntos += 1
    p.seek(p.tell()+2)
    pA = p.tell()
    co = -1
    while c != ",":
        co += 1
        c = p.read(1)
    p.seek(pA)
    actor = p.read(co)
    print(actor)

    dosPuntos = 0
    while dosPuntos < 11:
        c = p.read(1)
        if c == ":":
            dosPuntos += 1
    p.seek(p.tell()+2)
    rating = p.read(2)
    print("Rating: ", rating)
    dosPuntos = 0
    
    while dosPuntos < 9:
        c = p.read(1)
        if c == ":":
            dosPuntos += 1
    p.seek(p.tell()+2)

    pR = p.tell()
    co = -1
    while c != '"':
        co += 1
        c = p.read(1)
    p.seek(pR)
    recauda = p.read(co)
    print("Recaudación: ", recauda)

p.close()
