"""
Según la consigna del ejercicio 12 de la Guía 5,
que dice:
Cargar en listas los nombres y fechas de
nacimiento de varias personas, luego recorrerlo
y mostrar los nombres de los mayores de edad.
Funciones de carga y cálculo de edad.

Reformulen la solución utilizando almacenamiento
en archivo de texto. Para ello:
1) Escriban un programa de carga, que tome los
datos solicitados al usuario y los almacene en
un archivo de texto en el formato que prefieran. 
Pueden previamente almacenarlos en listas o no,
es opcional.
2) Escriban un segundo programa que tendrá como
salida los nombres de los mayores de edad.
Para ello, deberán leer el archivo creado en el
punto 1 y reutilizar la o las funciones que 
hayan escrito para la salida original.
"""


def namesAndAges():
    text = open('namesAndAges.txt', 'w')
    array = []
    confrmation = input('Do you like to upload any data? (y/n) ')
    while confrmation == 'y':
        array.append(input("What's your name? ")+', ')
        array.append(input("What's your age? ")+'\n')
        text.writelines(array)
        array = []
        confrmation = input('Do you like to upload more data? (y/n) ')


def readText(name):
    text = open(name+'.txt', 'r')
    names = []
    ages = []
    line = ' '
    while line != '':
        line = text.readline()
        if line != '':
            array = line[:-1].split(', ')
            names.append(array[0])
            ages.append(int(array[1]))
            print(names, ages)
    return(names, ages)


def ageing(names, ages):
    legalAge = []
    for i in range(len(ages)):
        if ages[i] >= 18:
            legalAge.append(names[i])
    return legalAge


namesAndAges()
names, ages = readText('namesAndAges')
print("People who have more than 18 are", ageing(names, ages))
