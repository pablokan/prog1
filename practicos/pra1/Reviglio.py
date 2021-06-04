def reposName(lista):
    l=[]
    for i in range(len(lista)):
        x=lista[i].split(',')
        y=x[1]
        final=y[1]+'. '+x[0]
        l.append(final)
    return l
       
def filtroListasParalelas(lista1,lista2,valor):
    l=[]
    for i in range(len(lista2)):
        if lista2[i]==valor:
            l.append(lista1[i])
    return l

def calculoPromEdad(lista):
    año=2021
    prom=0
    sumatoria=0
    c=0
    for i in range(len(lista)):
        x=lista[i].split('/')
        p=año-(int(x[2]))
        sumatoria=sumatoria+p
        c=c+1
    prom=int(sumatoria/c)
    return prom

def nombrePilaMasLargo(lista):
    nombre=''
    for i in range(len(lista)):
        x=lista[i].split(',')
        y=x[1].split()
        if len(y[0])>len(nombre):
            nombre=y[0]
    return nombre

nombres=['Torres, Ana', 'Hudson, Kate','Quesada, Benicio','Campoamores, Susana','Santamaría, Carlos','Skarsgard, Azul','Catalejos, Walter']
sexo=['f','f','m','f','m','f','m']
fecha=['02/05/1943','07/09/1984','10/02/1971','21/12/1967','30/01/1982','30/08/1995','18/07/1959']
l=[]

l=reposName(nombres)
print('Iniciales y apellidos de las personas: ')
for i in range(len(nombres)):
    print(l[i])
print('El nombre de pila más largo es:',nombrePilaMasLargo(nombres))
print('El promedio de edad de las mujeres es:',calculoPromEdad(filtroListasParalelas(fecha,sexo,'f')))
