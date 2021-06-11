import os
os.system('cls')
from datetime import date

def carga(cantidad):
    nombres=[]
    fechas=[]
    for i in range(0,cantidad):
        nombre=input('Nombre de persona: ')
        nombre=nombre+'\n'
        nombres.append(nombre)
        fecNac = input('Fecha de nacimiento (dd-mm-aaaa): ')
        fecNac=fecNac+'\n'
        fechas.append(fecNac)
    return nombres, fechas

def edad(listaFec):
    hoy = date.today()
    dn, mn, an = listaFec.split('-')
    dn = int(dn)
    mn = int(mn)
    an = int(an)
    dh = hoy.day
    mh = hoy.month
    ah = hoy.year
    e = ah - an
    if (mn > mh) or (mn == mh and dn > dh):
        e = e-1
    return e    

