def inputInt(mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = int(numero)
            validado = True
        except:
            print("Error. Debe ingresar un número entero")
    return numero
def inputFloat(mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            numero = float(numero)
            validado = True
        except:
            print("Error. Debe ingresar un número real")
    return numero
def inputFecha(mensaje):
    a='usando el formato dd/mm/aaaa'
    l=10
    seguir=True
    while seguir:
        print(mensaje,a)
        x=input()
        if ((x[2]=='/') and (x[5]=='/')) and len(x)==l:
            seguir = False
        else:
            print('Error. El formato ingresado es incorrecto.')
            seguir=True
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
def loadTxt(mensaje1,tipo1,mensaje2,tipo2,nombre):
    continuar=True
    f= open(nombre,'w')
    while continuar:
        if tipo1 == 'real' :
            var=inputFloat(mensaje1)
        elif tipo1=='entero':
            var=inputInt(mensaje1)
        elif tipo1=='fecha':
            var=inputFecha(mensaje1)
        else:
            var=input(mensaje1)
        f.write(var+',')
        if tipo2 == 'real' :
            var=inputFloat(mensaje2)
        elif tipo2=='entero':
            var=inputInt(mensaje2)
        elif tipo2=='fecha':
            var=inputFecha(mensaje2)
        else:
            var=input(mensaje2)
        f.write(var+',')
        continuar=inputContinuar()
    f.close()
    

listado=[]
str1='Ingrese el nombre: '
str2='Ingrese la fecha de nacimiento'
a=loadTxt(str1,'texto',str2,'fecha','nombres.txt')
