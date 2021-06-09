archivo = open('usu.csv', 'r') # modo lectura
# readlines

print("readlines------------------------")
print("puntero linea 4:", archivo.tell()) # devuelve cero porque estoy al principio del archivo
lineas = archivo.readlines() # devuelve una lista donde cada elemento es una fila del archivo convertida en string
print("puntero linea 6:", archivo.tell()) # devuelve la posición final del archivo
print(lineas, end="\n\n")  
print(lineas[5])

# reproduzco todo el archivo de texto en la salida del programa
for li in lineas:
    li = li[:-1] # le saco el último caracter (salto de línea)
    print(li)
print()
for li in lineas:
    if li[0] == "b":
        print(li)

# readline
print("readline--------------------------") # sin S final
linea = " "
archivo.seek(0) # volver al comienzo
while linea != "":
    linea = archivo.readline()
    print("Posición del puntero:", archivo.tell())
    if "Karen" in linea:
        print(linea)
