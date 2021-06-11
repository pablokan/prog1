def carga():
    nombres = ['Juan', 'Ana', 'Joaquin', 'Marta', 'Ricardo']
    fechas = ['02/05/1943', '07/09/1984', '10/02/1971', '21/12/2010', '30/01/2009']
    return nombres, fechas

n, f = carga()

archivo = open('nombres.txt', 'w')
archivo2 = open('fechas.txt', 'w')

for x in range(len(n)):    
    archivo.write(n[x]+'\n')
    archivo2.write(f[x]+'\n')
