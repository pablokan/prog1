import os
os.system('cls')

# Reformulen la solución utilizando almacenamiento en archivo de texto. Para ello:

#2) Escriban un segundo programa que tendrá como salida los nombres de los mayores de edad. Para ello, deberán leer el archivo creado en el punto 1 y reutilizar la o las funciones que hayan escrito para la salida original.


from carga_datos import edad

# 1) Escriban un programa de carga, que tome los datos solicitados al usuario ....
from carga_datos import carga # funcion de carga importada de archivo carga_datos

# ....se almacenan en un archivo de texto (fichas.csv) en el formato que prefieran.

listaNombres=open('fichas.csv','w')
qty=input('Cuantas personas integran la lista? ')
qt=int(qty)
listaNom, listaFec=(carga(qt))
listaNombres.writelines(listaNom)
listaNombres.close()
listaFechas=open('fichas.csv','a')
listaFechas.writelines(listaFec)
listaFechas.close()


