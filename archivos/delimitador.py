import csv

archivo = open("datitos.txt", "r")
filas = csv.reader(archivo, delimiter="%")

for fila in filas:
    print(fila)

archivo.close()
