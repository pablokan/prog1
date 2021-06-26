def inputInt(mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = int(numero)
            validado = True
        except:
            print("Error. Debe ingresar un número")
    return numero

def menuControlGenero():
    print('Ingrese el genero que desea buscar: ')
    print('1- Accion')
    print('2- Ciencia Ficcion')
    print('3- Comedia')
    x=inputInt('Ingrese la opcion deseada:\n')
    while x<1 or x>3:
        x=inputInt('Por favor, ingrese una opcion valida.\n')
    return x
def inputContinuar():
    seguir=True
    x='l'
    while seguir and x not in 'SsNn':
        x= input('¿Desea ingresar mas datos? s/n: ')
        if x in 'sS':
            seguir = True
        elif x in 'nN':
            seguir= False
        else:
            print('Error. El valor ingresado es incorrecto. ')
            seguir=True
    return seguir 

def transfor(valor,dicc):
    l=[]
    for keys in dicc:
        l.append(keys)
    p=''
    if valor ==1:
        p=l[0]
    elif valor==2:
        p=l[1]
    else:
        p=l[2]
    return p

def findGenero(valor, contenedor):
    l=[]
    for i in range(len(contenedor)):
        if valor in contenedor[i]:
            l.append(contenedor[i])
    return l

def truncarMostrar(contenedor,valor):
    l=[]
    x=[]
    for i in range(len(contenedor)):
       x=contenedor[i].split(valor)
       l.append(x[0])
    return l

def peliXGenero(contenedor,dicc):
    l=[]
    cont=False
    x=menuControlGenero()
    y=transfor(x,dicc)
    l=findGenero(y,contenedor)
    l=truncarMostrar(l,'(')
    y=dicc[y]
    print('Las peliculas de',y,'son: ')
    for i in range(len(l)):
        print(l[i])
    cont=inputContinuar()
    return cont

def soloNums(lista,valor):
    l=[]
    p=''
    for i in range(len(lista)):
        for a in range(len(lista[i])):
            if (lista[i])[a] in '$%1234567890(:,':
                if (lista[i])[a] == valor:
                    p=''
                else:
                    p=p+(lista[i])[a]
        l.append(p)
    return l

def anterioresAño(contenedor,año,valor):
    l=[]
    l2=[]
    l2=soloNums(contenedor,valor)
    for i in range(len(contenedor)):
        if año >int(l2[i]):
            l.append(contenedor[i])
    return l

def mostrarAntAño(contenedor):
    l=[]
    l2=[]
    cont=False
    año=inputInt('Ingrese el año de busqueda: ')
    l=anterioresAño(contenedor,año,'(')
    if len(l)!=0:
        l2=truncarMostrar(l,'(')
        print('Las peliculas anteriores al año',año,'son:')
        for i in range(len(l)):
            print(l2[i])
    else:
        print('No hay peliculas anteriores al año ingresado.')
    cont=inputContinuar()
    return cont

def letraNombre(valor,cont):
    l=[]
    for i in range(len(cont)):
        if (cont[i])[0]==valor:
            l.append(cont[i])
    return l

def readGenero(cont,dicc):
    l=[]
    l2=[]
    x=''
    for i in range(len(cont)):
        l2=cont[i].split(')')
        x=dicc[l2[1]]
        l.append(x)
    return l

def mostrarPorLetra(lista,diccionario):
    l=[]
    g=[]
    a=[]
    cont=False
    print('Ingrese la letra sobre la que desea realizar la busqueda:')
    letra=input()
    letra=letra.upper()
    l=letraNombre(letra,lista)
    g=readGenero(l,diccionario)
    a=soloNums(l,'(')
    l=truncarMostrar(l,'(')
    print('Las peliculas cuya nombre empieza con la letra',letra,'son: ')
    for i in range(len(l)):
        print(l[i],' Año: ',a[i],' Genero: ',g[i])
    cont=inputContinuar()
    return cont

def printMenu():
    print('Bienvenido,¿Que desea realizar?')
    print('1- Buscar las peliculas de un genero determinado.')
    print('2- Saber que peliculas se realizaron antes de un año especifico.')
    print('3- Identificar las peliculas que comiencen con una letra seleccionada.')
    x=inputInt('')
    while x<1 or x>3:
        x=inputInt('Por favor, ingrese una opcion valida.\n')
    return x

# def clearScrn():
#     x=0
#     while x<=10:
#         print(' \n')
#         x=x+1
#Idear forma de limpiar pantalla mas efectiva.
    
def menu(lis,dic):
    seguir=True
    c=0
    op=0
    while seguir:
        op=printMenu()
        if op==1:
            seguir=peliXGenero(lis,dic)
        elif op==2:
            seguir=mostrarAntAño(lis)
        else:
            seguir=mostrarPorLetra(lis,dic)
    c=c+1
    print('Ejecucion finalizada.')
    input()



movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
"Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
"Three Kings(1999)act", "The green hornet(2011)com"
]
genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}

menu(movies,genre)
