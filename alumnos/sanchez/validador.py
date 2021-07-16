import os
os.system('cls')

def concatenacion(*args,sep=' '):       
    estrings=''    
    for a in args:
        estrings=estrings+a+sep
    return estrings

def inputNumber(valor):
    cifra = input(valor)
    conjunto=False
    while not conjunto:
        try:
            entero = int(cifra)
            conjunto=True
        except:
            print("Error. Debe ingresar un número entero")
            cifra=input('Ingrese un entero nuevamente ')
    return entero
 
def selecta(value):   
    grupo=False
    while not grupo:
        if value >=7:
            erro=int(input("Error. Debe ingresar un número entre 1 y 6 : "))
            value=erro
        else:
            grupo=True
    return int(value)

def inputMail(correo):
    imail = input(correo)
    
    dire=False
    while not dire:
        arroba=imail.find('@')
        punto=imail.find('.')
        if arroba>0 and punto-arroba>0:
            dire=True            
        else:
            print('Error. El correo debe contener una "@" y un servidor.')
            imail=input('Ingrese nuevamente el mail ')
    return imail

def creaMenu(**kwargs):
    for k , v in kwargs.items():
        print(v)

def inputOp(elec):
    eleccion = input(elec)
    seg=True
    op=False
    while not op:
        if eleccion == 'si' or eleccion == 'SI' or eleccion == 's' or eleccion == 'S':
            seg=False
            op=True
        elif eleccion == 'no' or eleccion == 'NO' or eleccion == 'n' or eleccion == 'N':
            op=True       
        else:
            print('Opción errónea!!!. Debe indicar SI, NO, A VECES')
    return seg

def inputDate(dates):
    validado=False
    dates = 'Ingrese una fecha respentando el formato (dd/mm/aaaa): '
    while not validado:
        calendar = input(dates)
        if calendar[2]!='/' or calendar[5] != '/' or len(calendar)!= 10:
            print('Debe respetar el formato (dd/mm/aaaa): ')
        else:
            fechado = calendar.split('/')
            try:
                dya=int(fechado[0])
                mez=int(fechado[1])
                anio=int(fechado[2])
                validado=True
            except:
                print('Ingrese caracteres numericos')
    return dya , mez, anio            

def inputLstring(password):
    validado=False
    clave=input(password)
    print(clave)
    while not validado:
        c=len(clave)
        print(clave)
        if c >= 3 and c <= 6:
            validado=True
        else:
            clave=input('Error. Debe ingresar una cadena de al menos 3 caracteres, y no mas de 6: ')
    print(clave)
    return clave

