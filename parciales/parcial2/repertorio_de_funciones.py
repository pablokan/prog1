from math import inf
def inputNumber(mensaje,tipo,min=0,max=inf):
    #input de numero con validacion
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            if tipo == "entero" and (int(numero)>=min and int(numero)<=max):
                numero = int(numero)
                validado=True
            elif tipo == "real" and (float(numero)>=min and float(numero)<=max):
                numero = float(numero)
                validado=True
        except:
            print("Error. Your number does not match the requirements.")
    return numero

from datetime import date
def dateIn():
    #FUNCION validacion de formato fecha dd/mm/yyyy                       
    validado=False
    while validado==False:
        try: 
            fecha=input("Enter a date(dd/mm/yyyy): ")
            dia=int(fecha[:2])
            mes=int(fecha[3:5])
            anio=int(fecha[6:10])
            dia=fecha[:2]
            mes=fecha[3:5]
            anio=fecha[6:10]
            if fecha[2]!="/" or fecha[5]!="/":
                print("Make sure to enter the date using the dd/mm/yyyy format you dumb fuck!")
            else:
                validado=True
        except:
            print("Make sure to enter the date using the dd/mm/yyyy format you dumb fuck!")
    return(dia,mes,anio) 

def validacion(fecha):
    #validacion de fecha.Toma tupla yyyy/mm/dd 
    if int(fecha[1])<1 or int(fecha[1])>12 or int(fecha[0])<1 or int(fecha[0])>31 or ((int(fecha[1])==4 or int(fecha[1])==6 or int(fecha[1])==9 or int(fecha[1])==11) and int(fecha[0])>30) or (int(fecha[0])>29 and int(fecha[1])==2) or ((int(fecha[0])==29 and int(fecha[1])==2) and ((int(fecha[2])%100==0 and int(fecha[2])%400!=0) or (int(fecha[2])%100!=0 and int(fecha[2])%4!=0))):
        result="WRONG DATE."
    else:
        fechaFormato=""
        for x in reversed(fecha):
            fechaFormato=fechaFormato+str(x)+"/"
        result=fechaFormato[:-1]
    return result

def lenValIn(mensaje,min=0,max=inf):    
    #input de strings (validar largo por mínimo y/o máximo)
    vali=False
    while vali==False:
        strIn=input(mensaje)
        if len(strIn)<min or len(strIn)>max:
            print("Non validated.")
        else:
            vali=True
    return strIn

def valHora(mensaje):
    #input de hora con validacion de formato y hora. 
    validado=False 
    while not validado:
        hora=input(mensaje)
        try:
            if (int(hora[0:2])>=00 and int(hora[0:2])<=23) and (int(hora[3:5])>=00 and int(hora[3:5])<=59) and hora[2]==":":
                validado=True
        except:
            print("Hora incorrecta.")
    return hora

def cantRenglones(archivoTxt):
    #lee los dos archivos de texto y cuenta la cantidad de tareas que poseen en conjunto
    cont=0
    with open(archivoTxt) as file:
                line=file.readline()
                while line:
                    line=file.readline()
                    cont+=1
    return cont

def eliminarRenglon(archivoTxt,numeroDeRenglon):
    #Eliminar renglon especifico de Txt
    with open(archivoTxt) as file:    
        lines=file.readlines()
        del lines[numeroDeRenglon-1]
    with open(archivoTxt,"w") as file:
        for line in lines:
            file.write(line)

from os import system, name
def clear(): #clear de menu
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')