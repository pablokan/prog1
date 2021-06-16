f = open('pelis.json', 'r')
lineas = f.readlines()
f.close()
f = open('pelis.csv', 'w')
f.write('Nombre,Actor,Rating,Recaudacion\n')
for linea in lineas:
    posTitle = linea.find('Title')
    if posTitle != -1:
        peli = linea[posTitle+9: -3]
    if 'Actors' in linea:
        actor = linea[19: linea.find(',')]
    if 'Value' in linea and linea[-3] == '%':
        rotten = linea[-5:-3]
    caja = ''
    if 'BoxOffice' in linea:
        for caracter in linea:
            if caracter.isdigit():
                caja += caracter
        newLine = peli + ',' + actor + ',' + rotten + ',' + caja + '\n'
        f.write(newLine)
f.close()


