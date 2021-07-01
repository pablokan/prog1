f = open('practicos/practico8/nacidos.csv', 'r')
t = f.readlines()
f.close()
t.pop(0)

def verano(fecha): # formato aaaa-mm-dd
    retorno = 0
    anio, mes, dia = list(map(int, fecha.split('-')))
    if mes == 12 and dia >= 21:
        retorno = anio + 1
    elif (1 <= mes <= 2) or (mes == 3 and dia <=20):
        retorno = anio
    else:
        retorno = -1
    return retorno
 
c = 0 
a = 1985
for l in t:
    p = l.split()[0]
    nombre = p[:p.find(',')]
    fN = p[-10:]
    if verano(fN) == a:
        print(nombre)
    if verano(fN) != -1:
        c += 1
print('Y para Alexis, todos los nacidos en verano, sea el año que sea, son', c)
