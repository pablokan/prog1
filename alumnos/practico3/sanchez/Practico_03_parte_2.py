import os
os.system('cls')

#2) Escriban un segundo programa que tendrá como salida los nombres de los mayores de edad. Para ello, deberán leer el archivo creado en el punto 1 y reutilizar la o las funciones que hayan escrito para la salida original.

from carga_datos import carga, edad # funcion de cálculo de edad

# Recupero los datos del archivo de texto

datos=open('fichas.csv','r')
data=[]
linea=' '
while linea!='':
    linea=datos.readline()
    linea=linea[:-1]
    data.append(linea)      # Asigno los elementos a una lista
q=len(data)-1               # por algun motivo la lista me agrega un elemnto vacio al final
s=int(q/2)                  # por la estructura asigne la mitad de la lista a fechas
for i in range(s,q):
    if edad(data[i])>18:
        print(data[i-s], 'es mayor de edad.')
