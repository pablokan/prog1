nombresCompletos = ['Torres, Ana', 'Hudson, Kate', 'Quesada, Benicio', 'Campoamores, Susana', 'Santamaría, Carlos', 'Skarsgard, Azul', 'Catalejos, Walter']
sexos = ['f','f','m','f','m','f','m']
fechas = ['02/05/1943', '07/09/1984', '10/02/1971', '21/12/1967', '30/01/1982', '30/08/1995', '18/07/1959']

# 1) Solución 1
nombres = []
for nombre in nombresCompletos:
    posComa = nombre.find(",")
    salida = nombre[posComa + 2] + '. ' + nombre[:posComa]
    nombres.append(nombre[posComa + 2:])
    print(salida)
# 1) Solución 2
for x in range(len(nombresCompletos)):
    nombreCompleto = nombresCompletos[x].split(', ')
    nombre = nombreCompleto[1]
    apellido = nombreCompleto[0]
    salida = nombre[0] + ". " + apellido
    print(salida)

# 2) Decir el nombre de pila mas largo
nombreMasLargo = ""
for nombre in nombres:
    print(nombre, len(nombre))
    if len(nombre) > len(nombreMasLargo):
        nombreMasLargo = nombre
print(nombreMasLargo)

from calcula_edad import edad
tE = 0
cM = 0
for i in range(len(sexos)):
    if sexos[i] == 'f':
        tE += edad(fechas[i])
        cM += 1 # cM = cM + 1

print(tE // cM)



