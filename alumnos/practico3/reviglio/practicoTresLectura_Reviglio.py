def txtToList(nombre):
    l=[]
    f=open(nombre,'r')
    x=' '
    while x!='':
        x=f.read()
        l.append(x)
    f.close()
    return l
def calculoEdad(lista):
    año=2021
    pos=[]
    for i in range(len(lista)):
        x=lista[i].split('/')
        p=int(x[2])
        if (año-p)>=18:
            pos.append(i)
    return pos
def mostrarPosicionesLista(lista, pos):
    x=''
    for i in range(len(pos)):
        if i!=(len(pos)-1):
            x=x+str(lista[pos[i]])+', '
        else:
            x=x+str(lista[pos[i]])+'.'
    return x
def purgarLista(lista,valor):
    l=[]
    for i in range(len(lista)):
        if lista[i]!=valor:
            l.append(lista[i])
    return l
def splitear(lista,valor):
    l=[]
    l2=[]
    x=lista[0].split(valor)
    c=0
    for i in range(len(x)):
        if c==0:
            l.append(x[i])
            c=1
        else:
            l2.append(x[i])
            c=0
    return l, l2
listado=[]
listadoFinal=[]
listado=purgarLista(txtToList('nombres.txt'),'')
listadoFinal=splitear(listado,',')
pos=calculoEdad(listadoFinal[1])
x=mostrarPosicionesLista(listadoFinal[0], pos)
print('Los mayores de edad son:',x)