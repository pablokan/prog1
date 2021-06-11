# guia 5 ej 12
# Cargar en listas los nombres y fechas de nacimiento de varias personas, 
# luego recorrerlo y mostrar los nombres de los mayores de edad. 
# Funciones de carga y cálculo de edad.

#practico 3 ej 1
#Reformulen la solución utilizando almacenamiento en archivo de texto. Para ello:
# 1) Escriban un programa de carga, que tome los datos solicitados al usuario y los 
# almacene en un archivo de texto en el formato que prefieran. Pueden previamente 
# almacenarlos en listas o no, es opcional.

from archivotexto import crearArchivo,guardarInfoEnTexto

def carga():
    nombres = ['Juan', 'Luisa', 'Ana', 'Pedro']
    fecNac = ['07-02-2004', '13-09-1991', '17-10-2012', '04-04-1963']
    return nombres, fecNac
#coloco la funcion de carga que ya tenia echa pero use el ejemplo que usted paso
#por comodidad para no tener que poner los nombres y fechas cada vez que revisaba algo
# def carga():
#     lNombres = []
#     lFechanac = []
#     respuesta = "s"
#     while respuesta == "s":
#         nombre = input("ingrese nombre: ")
#         lNombres.append(nombre)
#         fechaNac = input("ingrese fecha de nacimiento de la forma dd-mm-aaaa: ")
#         lFechanac.append(fechaNac)
#         respuesta = input("desea ingresar otro dato (s/n)")
#     return lNombres,lFechanac
def guardarNombreFechaNac (listaNombres,listaFechaNacimiento,nombreTexto):
    for i in range(len(listaNombres)):
        guardarInfoEnTexto(listaNombres[i],nombreTexto)
        guardarInfoEnTexto(listaFechaNacimiento[i],nombreTexto)


nomTexto = input("ingrese el nombre del archivo de texto: ")
nombres,fechaNacimiento = carga()
crearArchivo(nomTexto)
guardarNombreFechaNac(nombres,fechaNacimiento,nomTexto)
