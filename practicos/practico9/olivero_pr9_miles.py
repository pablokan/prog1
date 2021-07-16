#OLIVERO, EZEQUIEL 14/07/2021
import random
from math import inf

def lenValIn(mensaje,min=0,max=inf):
    #input de strings (validar largo por mínimo y/o máximo)
    vali=False
    strIn = ''
    while vali==False:
        strIn=input(mensaje)
        if len(strIn)<min or len(strIn)>max:
            print("Non validated.")
        else:
            vali=True
    return strIn

def inputNumber(mensaje,tipo,min=0,max=inf):
    #input de numero con validacion
    validado = False
    numero = ""
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

def milesNumGen():
    #generador de numero MILES
    numeroStr="11"
    while (numeroStr[0]==numeroStr[1] or numeroStr[0]==numeroStr[2] or numeroStr[0]==numeroStr[3]) or (numeroStr[1]==numeroStr[2] or numeroStr[1]==numeroStr[3]) or (numeroStr[2]==numeroStr[3]):
        numeroStr=str(random.randint(1000,9999))
    return numeroStr

def compara(valor1,valor2):
    #comparador de str, toma dos argumentos
        if valor1==valor2:
            print("EXITO!")
            return False
        else:
            for letra in range(len(valor1)):      
                if valor1[letra]==valor2[letra]:
                    print("BIEN")
                elif valor1[letra] in valor2:
                    print("REGULAR")

def ranking(dic):
    #recive diccionario y lo printea piola
    posicion=1
    print("\n==>SCORE RANKING<==")
    for key,value in (list(dic.items())[0:10]):
        print(f"{posicion}-{key}, score: {value}")
        posicion+=1
    print("<=================>\n")
    
def miles(dic): #juega, recive diccionario para agregar el score de la partida
    intentos=0    
    vali=False
    numeroRandom=milesNumGen()
    while vali==False:
        intentos+=1
        if compara(numeroRandom,str(inputNumber("Ingrese numero de 4 digitos: ","entero",min=1000,max=9999)))==False:
            vali=True
    print(f"Finalizado, Intentos/Score: {intentos}")
    with open("ranking.txt","a") as file:
        file.write(lenValIn("Ingrese su nombre: ",min=0,max=25)+":"+str(intentos)+"\n")        
 
def menuMiles(*args):
    #menu principal try de abrir el txt con los scores y leerlo, except lo crea si no existe
    scores={}
    eleccion=0
    while eleccion!=3:
        try:
            with open("ranking.txt") as file:    
                archivoScores = file.readlines()
                for dato in range(len(archivoScores)):
                    separador=archivoScores[dato].find(":")
                    nombre=(archivoScores[dato][0:separador])
                    score=(archivoScores[dato][separador+1:-1])
                    scores[nombre]=score
        except:
            open("ranking.txt","x")            
        for x in args:
            print(x)
        eleccion=inputNumber("Seleccione opcion 1-3: ","entero",min=1,max=3)
        if eleccion==1:
            miles(scores)
        if eleccion==2:
            ranking(dict([(key, value) for (key, value) in sorted(scores.items(), key=lambda x: x[1])]))

menuMiles("1-Jugar","2-Ranking","3-Quit")

