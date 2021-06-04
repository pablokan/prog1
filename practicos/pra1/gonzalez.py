from abc import abstractproperty


nombres = ["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana","Santamaría, Carlos","Skarsgard, Azul","Catalejos, Walter"]
sexos = ["f","f","m","f","m","f","m"]
fechas = ["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
aux = []
aux2 = []
cadena = ""
for x in range(len(nombres)):
    aux = nombres[x].split(",")
    cadena = aux[1]
    cadena = list(cadena)
    aux2.append(cadena)
    cadena = cadena[1] + ". " + aux[0]

print(aux2)
aux = []
cadena = ""
mayor = 0
n = 0
suma = 0
for x in range(len(aux2)):
    for x in range(len(aux2[x])):
        suma = suma + 1
        if suma > mayor:
            mayor = suma
            aux.append(aux2[x])

    