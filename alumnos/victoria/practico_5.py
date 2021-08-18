archivo = open ('pelis.json', 'r')
lineas = archivo.readlines()
archivo.close
titulos = ''
actores = ''
ratingTotten = ''
recaudacion = ''
#print(lineas)
nuevoArchivo = open('pelis.csv','w')
nuevoArchivo.write('Nombre,Actor,Rating,Recaudacion\n')
for lin in lineas:
    #print(lin)
    #PRIMERO ENCUENTRO LOS TITULOS
    posTitulo = lin.find('Title')
    if posTitulo != -1:
        titulos = lin[posTitulo+9:-3]

    #NOMBRE DE ACTORES
    posActor = lin.find('Actors')
    if posActor != -1:
        posComa = lin.find(',')
        actores = lin[posActor+10:posComa]

    #RATING DE ROTTEN TOMATOES
    posValor = lin.find('Value')
    if posValor != -1:
        rating = lin[posValor+9:-2]
        #print(rating)
        if '%' in rating:
            ratingTotten = rating
            ratingTotten = ratingTotten[:-1]


    #RECAUDACION
    posRecaudacion = lin.find('BoxOffice')
    if posRecaudacion != -1:
        recaudacion = lin[posRecaudacion+14:-3]

    #POR QUE NO FUNCIONAAAAAAAAAA
nuevaLinea = titulos + ',' + actores + ',' + ratingTotten + ',' + recaudacion + '\n'
print(nuevaLinea)
nuevoArchivo.write(nuevaLinea)

nuevoArchivo.close 
