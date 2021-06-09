a = open("t01.txt", "r")
print("Posición:", a.tell()) # posición del puntero
todo = a.read() # "Juan\nPedro\n"

print("Posición:", a.tell())
for i in range(len(todo)):
    print(i, ord(todo[i]), todo[i])
print("fin")

posi = 2
a.seek(posi) # moverse a la posición
letra = a.read(1) # leer un caracter
print("letra en la posición", posi, ":", letra)


a.seek(0)
c = " "
cadena = ""
while c !="":
    c = a.read(1)
    if c != "" and ord(c) != 10:
        cadena += c
print(cadena)

a.close()
