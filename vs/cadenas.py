nombresCompletos = ['Torres, Ana', 'Hudson, Kate', 'Quesada, Benicio', 'Campoamores, Susana', 'Santamaría, Carlos', 'Skarsgard, Azul', 'Catalejos, Walter']

for i in range(len(nombresCompletos)):
    nombreCompleto = nombresCompletos[i]
    posComa = nombreCompleto.find(',')
    posInicial = posComa + 2
    inicial = nombreCompleto[posInicial]
    apellido = nombreCompleto[0:posComa]
    nombre = nombreCompleto[posInicial:]
    nuevoNombre = inicial + '. ' + apellido
    print(nombre)








