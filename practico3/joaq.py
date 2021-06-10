#1) Escriban un programa de carga, que tome los datos solicitados al usuario
# y los almacene en un archivo de texto en el formato que prefieran. 
# Pueden previamente almacenarlos en listas o no, es opcional.


def cargaPersonas (nombre,fecha):
    file =open('tp3.txt','w') 
    nameslist = [] 
    borninglist = []
    resp = "si"
    while resp == "si":
        nombre = input("ingrese los nombres:")
        nameslist.append(nombre)
        file.write('nombres:%s \n'%nombre)
        fecha = input("ingrese la fecha de nacimiento en formato guiones (05-07-1890):")
        borninglist.append(fecha)
        file.write('fechas:%s \n'%fecha)
        resp = input("Desea cargar mas personas?: ")
    
    return nameslist , borninglist
    
name,dates = cargaPersonas("ingrese nombre","ingrese fecha")
#print (name,dates)

#2) Escriban un segundo programa que tendrá como
# salida los nombres de los mayores de edad. 
# Para ello, deberán leer el archivo creado en el punto 1 
# y reutilizar la o las funciones que hayan escrito para la salida original.

file = open('tp3.txt','r')
lecturaC = file.read()
file.close()
print (lecturaC)

""" 
from calcula_edad import edad

print ('las personas mayores de edad son:')
for x in range(len(name)):
    if edad(dates[x]) >= 18:
        print(name[x],'y sus años son:',edad(dates[x]))
"""