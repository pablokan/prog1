# Según la consigna del ejercicio 12 de la Guía 5, que dice:
# Cargar en listas los nombres y fechas de nacimiento de varias personas, luego recorrerlo y mostrar los nombres de los mayores de edad. 
# Funciones de carga y cálculo de edad.
# Reformulen la solución utilizando almacenamiento en archivo de texto. Para ello:
# 1) Escriban un programa de carga, que tome los datos solicitados al usuario y los almacene en un archivo de texto en el formato que prefieran.
#  Pueden previamente almacenarlos en listas o no, es opcional.
# 2) Escriban un segundo programa que tendrá como salida los nombres de los mayores de edad. 
# Para ello, deberán leer el archivo creado en el punto 1 y reutilizar la o las funciones que hayan escrito para la salida original.





nombre = ['Juan', 'Lucia', 'Ana', 'Daniel', 'Federico', 'Sonia']
fecha = ['07/02/2004', '13/09/1991', '17/10/2012', '04/04/1963', '28/07/1998', '20/03/2010']


def crear_archivo(nombres, fechas):
    archivo = open('practico.txt','w')   #crear archivo
    archivo.write(str(nombres))
    archivo.write('\n'+ str(fechas))
    archivo.close()
    
crear_archivo(nombre, fecha)
        
    
    
archivo = open('practico.txt', 'r')  #leer archivo
nom = archivo.readline()
fech = archivo.readline()
print(nom)
print(fech)
archivo.close()

from calcula_edad import edad

nom_mayores = []      

for i in range(len(nombre)):
    if edad(fecha[i]) >= 18:
        nom_mayores.append(nombre[i])
    
print(f'Los mayores de edad son: {nom_mayores}')