# guia 5 ej 12
# Cargar en listas los nombres y fechas de nacimiento de varias personas, 
# luego recorrerlo y mostrar los nombres de los mayores de edad. 
# Funciones de carga y cálculo de edad.

#practico 3 ej 2
#Reformulen la solución utilizando almacenamiento en archivo de texto. Para ello:
# 2) Escriban un segundo programa que tendrá como salida los nombres de los mayores 
# de edad. Para ello, deberán leer el archivo creado en el punto 1 y reutilizar la 
# o las funciones que hayan escrito para la salida original.

from calculaEdad import edad
from archivotexto import leerInfoTexto

def separarInfo (informacionASeparar):
    lista = informacionASeparar.split(",")
    return lista
def separarNombreFecha (listaSinSeparar):
    lNombres = []
    lFechaNac = []
    for i in range(len(listaSinSeparar)):
        if i % 2 == 0 :
            if listaSinSeparar[i] != "":
                lNombres.append(listaSinSeparar[i])
        else:
            lFechaNac.append(listaSinSeparar[i])
    return lNombres,lFechaNac
def mayoresDeEdad (lNombres,lFechanac):
    for i in range(len(lFechanac)):
        if edad(lFechanac[i]) >= 18:
            print(lNombres[i])

nomTexto = input("ingrese el nombre del archivo de texto: ")
informacion = leerInfoTexto(nomTexto)
informacion = separarInfo(informacion)
nombres,fechaNacimiento = separarNombreFecha(informacion)
print("los mayores de edad son: ")
mayoresDeEdad(nombres,fechaNacimiento)