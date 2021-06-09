a = open("omdb/palabras.txt", "r")
c = "nada"
lista = []

while c != "":
    c = a.read(1)
    p = ""

    while c.upper() in "abcdefghijklmnñopqrstuvwxyzáéíóú".upper() and c!="":
        p += c
        c = a.read(1)

    if p != "":
        lista.append(p)

print(lista)

a.close()

    