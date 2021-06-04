from calcula_edad import edad

nombres = ['Torres, Ana', 'Hudson, Kate', 'Quesada, Benicio', 'Campoamores, Susana', 'Santamaría, Carlos', 'Skarsgard, Azul', 'Catalejos, Walter']
sexos = ['f','f','m','f','m','f','m']
fechas = ['02/05/1943', '07/09/1984', '10/02/1971', '21/12/1967', '30/01/1982', '30/08/1995', '18/07/1959']

for nombreCompleto in nombres:
    posComa = nombreCompleto.find(',')
    nuevo = nombreCompleto[posComa+2] + '. ' + nombreCompleto[:posComa]
    print(nuevo)

largo = 0
nombreLargo = ''
for nombreCompleto in nombres:
    posComa = nombreCompleto.find(',')
    nombre = nombreCompleto[posComa+2:]
    if len(nombre) > largo:
        largo = len(nombre)
        nombreLargo = nombre
print(nombreLargo)

tE = 0
cM = 0
tt = 0
for x in range(len(sexos)):
    tt += edad(fechas[x])
    if sexos[x] == 'f':
        tE += edad(fechas[x])
        cM += 1

print(tE//cM)




