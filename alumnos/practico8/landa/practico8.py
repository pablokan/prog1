# Dado un archivo de texto en formato CSV (valores separados por coma), 
# realizar un programa que solicite un año entre 1980 y 1999 
# (ambos incluídos)y muestre los nombres de las personas nacidas 
# en el verano (considerar que el verano de un año incluye a los nacidos 
# desde el 21 de diciembre del año anterior).
# De preferencia (no es obligatorio), hacer una función que reciba una 
# fecha y que devuelva algún valor que sirva para determinar si 
# corresponde al verano del año pedido

from archivotexto import leerLineaTexto

def estacionDeNacimiento (fechaNacimiento):
    estacion = " no se modifico"
    mes = int(fechaNacimiento[fechaNacimiento.find(",")+6:fechaNacimiento.find(",")+8])
    dia = int(fechaNacimiento[fechaNacimiento.find(",")+9:fechaNacimiento.find(",")+11])
    if mes == 12 or (mes > 0 and mes < 4):
        if mes == 12 and dia > 20:
            estacion = "verano"
        elif mes == 3 and dia < 21:
            estacion = "verano"
        elif mes == 1 or mes == 2:
            estacion = "verano"
    elif mes > 2 and mes < 7:
        if mes == 3 and dia > 20:
            estacion = "otono"
        elif mes == 6 and dia < 21:
            estacion = "otono"
        elif mes == 4 or mes == 5:
            estacion = "otono"
    elif mes > 5 and mes < 10:
        if mes == 6 and dia > 20:
            estacion = "invierno"
        elif mes == 9 and dia < 21:
            estacion = "invierno"
        elif mes == 7 or mes == 8:
            estacion = "invierno"
    elif mes > 8 and mes < 13:
        if mes == 9 and dia > 20:
            estacion = "primavera"
        elif mes == 12 and dia < 21:
            estacion = "primavera"
        elif mes == 10 or mes == 11:
            estacion = "primavera"
    return estacion,mes

def solicitarAno():
    fechaPedida = 0
    while fechaPedida < 1980 or fechaPedida > 1999:
        fechaPedida = int(input("ingrese un año entre 1980 y 1999: "))
    return fechaPedida

def nacidosEnVerano(listaNacidos):
    fecha = solicitarAno()
    for nacidos in listaNacidos:
        if fecha == int(nacidos[nacidos.find(",")+1:nacidos.find("-")]):
            if estacionDeNacimiento(nacidos)[0] == "verano" and estacionDeNacimiento(nacidos)[1] != 12:
                print(nacidos[:nacidos.find(",")])
        elif fecha-1 == int(nacidos[nacidos.find(",")+1:nacidos.find("-")]):
            if estacionDeNacimiento(nacidos)[0] == "verano" and estacionDeNacimiento(nacidos)[1] == 12:
                print(nacidos[:nacidos.find(",")])


    

lista = leerLineaTexto("nacidos.csv")
lista.pop(0)
nacidosEnVerano(lista)

