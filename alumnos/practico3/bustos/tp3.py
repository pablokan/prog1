#  Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad. Funciones de carga y cálculo de edad.
# Reformulen la solución utilizando almacenamiento en archivo de texto. Para ello:
# 1) Escriban un programa de carga, que tome los datos solicitados al usuario y los almacene en un archivo de texto en el formato que prefieran. Pueden previamente almacenarlos en listas o no, es opcional.
# 2) Escriban un segundo programa que tendrá como salida los nombres de los mayores de edad. Para ello, deberán leer el archivo creado en el punto 1 y reutilizar la o las funciones que hayan escrito para la salida original.

nombres = []
fecha_de_nacimiento = []

print("Desea cargar datos? \n1: si \n2: no ")
res = int(input())

while res == 1:
    ingreso = input("Ingrese su nombre: ") + ' '
    nombres.append(ingreso)
    naciminento = input("Ingrese su fecha de nacimiento ") + ', '
    fecha_de_nacimiento.append(naciminento)
    print("Repito? \n1: si \n2: no")
    res = int(input())
    
print(nombres,fecha_de_nacimiento)


file = open('datos.csv', 'w')
file.writelines(nombres)
file.writelines(fecha_de_nacimiento)
file.close()

lista = open('datos.csv', 'r')
todo = lista.readlines()
print(todo)
