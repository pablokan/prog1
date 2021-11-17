import csv

archivo = open("datitos.txt", "r")
filas = csv.reader(archivo, delimiter="%")
info = filas
for fila in filas:
    print(fila)


archivo.close()

for x in info:
    print(x)
