f = open('deudores.txt', 'r')
todo = f.readlines() # lee todo y guarda en una lista de strings x fila
todo.pop(0) # elimina la fila de títulos
f.close()
d = open('morosos.txt', 'w')
d.write('nombre, mail, saldo\n')
for linea in todo:
    deudor = linea.split(',')
    deuda = int(deudor[4][1:-3])
    anio = deudor[5][-4:]
    #print(deuda, type(deuda), anio, type(anio))
    if deuda > 200000 and anio == '2019':
        grabar = deudor[1] + ',' + deudor[2] + ',' + str(deuda) + '\n'
        d.write(grabar)
d.close()




