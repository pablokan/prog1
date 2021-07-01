from valids import *

f = open('nacidos.csv', 'r')
t = f.readlines()
f.close()
t.pop(0)
    
def verano(fecha): # Recibe: aaaa-mm-dd Devuelve: año
    retorno = 0
    #a, m, d = list(map(int, fecha.split('-')))
    a, m, d = [int(e) for e in fecha.split('-')]
    if (m == 12 and d >= 21):
        retorno = a + 1
    elif (m == 1) or (m == 2) or (m == 3 and d <= 20):
        retorno = a
    else:
        retorno = -1
    return retorno

a = inputRangeInt('Ingrese un año entre 1980 y 1999: ', 1980, 1999)

for l in t:
    pC = l.find(',')
    nombre = l[:pC]
    fecha = l[pC+1: pC+11]
    if a == verano(fecha):
        print(nombre)



