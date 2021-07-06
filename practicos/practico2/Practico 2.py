import os
os.system('cls')

# La primera función debe realizar la conversión de la cadena de 2008 a lista o listas (que la salida sea similar a la lista o listas definidas para los datos de 2018)

def estadistica(regis):
    i=0
    lista08=regis.split(',')
    sex08f=[]
    sex08m=[]
    nam08f=[]
    nam08m=[]
    qty08f=[]
    qty08m=[]
    for i in range(2,30,3):
        namreg08=lista08[i-2]
        qtyreg08=lista08[i-1]
        sexreg08=lista08[i]
        if sexreg08 == 'f':
            nam08f.append(namreg08)
            qty08f.append(qtyreg08)
            sex08f.append(sexreg08)
        else:
            nam08m.append(namreg08)
            qty08m.append(qtyreg08)
            sex08m.append(sexreg08)
    return nam08f,qty08f,sex08f,nam08m,qty08m,sex08m

# La segunda función debe recibir como parámetros: año, posición, sexo. Y debe retornar: nombre, cantidad    

def nomq(reganio, orden, sex):
    if anio == '2018':
        if gen=='f':
            nom=n18f[pos]
            cant=q18f[pos]
        else:
            nom=n18m[pos]
            cant=q18m[pos]
    else:
        if gen=='f':
            nom=n08f[pos]
            cant=q08f[pos]
        else:
            nom=n08m[pos]
            cant=q08m[pos]
    return nom, cant

# La tercera función servirá para buscar un nombre en un año determinado. Devuelve verdadero o falso.

def busca(registro):
    if anio==2008:
        si=(esta in registro2008)
    else:
        si=(esta in registro2018)
    return si

# Registros almacenados en una sola variable para su conversion con la funcion "def estadistica(registroanio)"
 
registro2008 = 'Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f'

registro2018 = 'Liam,19837,m,Emma,18688,f,Noah,18267,m,Olivia,17921,f,Michael,14516,m,Ava,14924,f,James,13525,m,Isabella,14464,f,Oliver,13389,m,Sophia,13928,f'

# Matrices emergentes de las estadisticas de ambos años

n08f, q08f, s08f, n08m, q08m, s08m = estadistica(registro2008)
n18f, q18f, s18f, n18m, q18m, s18m= estadistica(registro2018)

# Datos a proveer por el operador
print('************************************')
anio = input('Estadistica del año: ')
ub = int(input('En que posición evalúa? '))
pos = ub-1
gen = input('Sexo del registro? ')
letrai=('Letra inicial a comparar: ')
esta=input('Nombre a buscar: ')
inicial=input('Inicial que quiere analizar: ')
print('************************************')
print('      ')

nombre, cantidad = nomq(anio, pos, gen)

# Requerimeinto 1: La diferencia en cantidad de bebés que existe entre los nombres de misma posición y mismo sexo.

for d in range(len(n08f)):
    if gen=='f':
        diferencia=int(q18f[pos])-int(q08f[pos])
        nommas=n18f[d]
        nomenos=n08f[d]
    else:
        diferencia=int(q18m[pos])-int(q08m[pos])
        nommas=n18m[d]
        nomenos=n08m[d]   
print('************************************')
print('      ')
print(diferencia, ' es la diferencia entre ', nommas, ' y ', nomenos, ' en la posición ', ub, ' del ranking de ', gen, 'de 2018 y 2008 respectivamente')

# Requerimiento 2: Los nombres de todos los bebés que comienzan con la misma letra considerando ambos periodos.



# Requerimiento 3: Los nombres que se repiten.

listacomp=n08f+n18f+n08m+n18m
listarep=[]
for r in range(len(listacomp)):
    for j in range(r+1,len(listacomp)):
        if listacomp[r]==listacomp[j]:
            a=listacomp[r]
            listarep.append(a)
print('      ')
print('************************************')
print('      ')
print('Se repiten los siguientes nombres: ', ' - '.join(listarep))

lista_inicial=[]
repetidos=[]
nueva_cadena = ""
for f in listacomp:
    nueva_cadena = nueva_cadena + f[0]    
#    print(p,'---------------')
#print(nueva_cadena)

for g in range(len(listacomp)):
    if inicial==nueva_cadena[g]:
        repetidos.append(nueva_cadena[g])
        a=listacomp[g]
        lista_inicial.append(a)
print('************************************')
print('      ')
print('Nombres con ', inicial, ':',' - '.join(lista_inicial) )