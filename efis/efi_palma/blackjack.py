import random
import time
from cartas import mostrar_cartas
from funciones import verCartasyPuntos, verReglas
class Cartas:
    def __init__(self, palo, valores, carta_valor):
        self.palo = palo
        self.valores = valores
        self.carta_valor = carta_valor
#Comienzo del juego
def blackjack(mazo):
    print("Preparate para jugar "+nombre+"!")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".\n")
    time.sleep(1)
    #-------------------------------------------------------------------
    time.sleep(1)
    jugador_cartas = [] #Creamos una lista con las cartas del jugador. 
    croupier_cartas = [] #Creamos una lista con las cartas del croupier.
    jugador_puntaje = 0 # Puntaje del jugador
    croupier_puntaje = 0 # Puntaje del croupier
    #-------------------------------------------------------------------
    while len(jugador_cartas) < 2:
        #Este primer ciclo se detiene hasta que el jugador tenga 2 cartas
        j_carta = random.choice(mazo) #selecciona una carta al azar
        jugador_cartas.append(j_carta) #agrega la carta a la lista de cartas del jugador
        mazo.remove(j_carta) #quita la carta del mazo
        jugador_puntaje += j_carta.carta_valor #suma el valor de la carta al puntaje del jugador
        if len(jugador_cartas) == 2: #si ya tienes 2 cartas
            if jugador_cartas[0].carta_valor == 11 and jugador_cartas[1].carta_valor == 11: # si sale un As en cada carta, la primera vale 1 
                #y la segunda vale 11, la suma total seria 12.
                jugador_cartas[0].carta_valor = 1
                jugador_puntaje -= 10 #restamos 10 al puntaje inicial del jugador(22-10=12)
        verCartasyPuntos(jugador_cartas,False,jugador_puntaje,nombre=nombre)
        #-------------------------------------------------------------------
        input()
        #un proceso similar se repite para el croupier, pero solamente mostramos la primera carta
        c_carta = random.choice(mazo)
        croupier_cartas.append(c_carta)
        mazo.remove(c_carta)
        croupier_puntaje += c_carta.carta_valor
        if len(croupier_cartas) == 1: #si dentro de la lista de cartas del croupier hay una sola,que la muestre.  
            verCartasyPuntos(croupier_cartas,False,croupier_puntaje,nombre="croupier")
        else:
            print("Cartas del croupier: ")
            mostrar_cartas(croupier_cartas[:-1], True)# si dentro de la lista de cartas del croupier hay 2 o mas cartas    
            print("Puntaje:", croupier_puntaje - croupier_cartas[-1].carta_valor)# que muestre la primera carta y solo ese puntaje de carta
        #Si el croupier tiene 2 cartas y el puntaje del jugador es distinto de 21(blackjack),evalua
        #si sale un As en cada carta, la primera vale 1 y la segunda vale 11, la suma total seria 12.
        if len(croupier_cartas) == 2 and jugador_puntaje !=21:
            if croupier_cartas[0].carta_valor == 11 and croupier_cartas[1].carta_valor == 11:
                croupier_cartas[1].carta_valor = 1
                croupier_puntaje -= 10
        #Luego de la primera ronda de 2 cartas, evaluamos si el jugador tiene blackjack
        if jugador_puntaje == 21 and croupier_puntaje != 21:
            print("FELICIDADES, has hecho un BLACKJACK!")
            time.sleep(2)
            print("El croupier no tenia blackjack..")
            verCartasyPuntos(croupier_cartas,False,croupier_puntaje)
            print(nombre, "Ganaste!")
            otrapartida()
        #Evaluamos la posibilidad de un empate en blackjack
        elif jugador_puntaje == 21 and croupier_puntaje == 21:
            print("Empate!")
            verCartasyPuntos(croupier_cartas,False,croupier_puntaje)
            otrapartida()
        input()
    #-------------------------------------------------------------------
    print()
    verCartasyPuntos(jugador_cartas,False,jugador_puntaje,nombre=nombre)
    # Una vez conocidas las primeras 2 cartas del jugador, tenemos que preguntarte si desea plantarse o pedir otra carta, 
    # mientras no se pase de los 21 puntos, en tal caso, pierde. 
    while jugador_puntaje < 21:
        print("Ingrese una de las siguientes opciones:"
                "\n1-Pedir carta"
                "\n2-Plantarse")
        respuesta=input("Opcion ingresada: ")
        while (respuesta != "1" and respuesta != "2"):
            print("Usted a ingresado una opcion incorrecta, solo puede ingresar las siguientes opciones:"
                  "\n1-Pedir carta"
                  "\n2-Plantarse")
            respuesta=input("Opcion ingresada: ")
        if respuesta == "1":
            j_carta= random.choice(mazo)
            jugador_cartas.append(j_carta)
            mazo.remove(j_carta)
            jugador_puntaje += j_carta.carta_valor
            c = 0
            while jugador_puntaje > 21 and c < len(jugador_cartas):
                if jugador_cartas[c].carta_valor == 11:
                    jugador_cartas[c].carta_valor = 1
                    jugador_puntaje -= 10
                    c += 1
                else:
                    c += 1 
            time.sleep(1)
            verCartasyPuntos(jugador_cartas,False,jugador_puntaje,nombre=nombre)
            time.sleep(2)
            if jugador_puntaje == 21 and croupier_puntaje != 21:
                print("FELICIDADES, has hecho un BLACKJACK!")
                time.sleep(2)
                print("El croupier no tenia blackjack..")
                verCartasyPuntos(croupier_cartas,False,croupier_puntaje)
                print(nombre, "Ganaste!")
                otrapartida()
            elif jugador_puntaje == 21 and croupier_puntaje == 21:
                print("Empate!")
                verCartasyPuntos(croupier_cartas,False,croupier_puntaje)
                otrapartida()
            elif jugador_puntaje > 21:
                print(nombre,"Perdiste! Te pasate de los 21 puntos..Mucha suerte la proxima!")
                verCartasyPuntos(croupier_cartas,False,croupier_puntaje)
                otrapartida() 
        if respuesta == "2":
            break
    #Al momento de decidirse plantarse, el croupier revela la segunda carta.
    time.sleep(1)
    print("croupier da vuelta su carta..espere..")
    time.sleep(2)
    verCartasyPuntos(croupier_cartas,False,croupier_puntaje)
    print("Presione enter para continuar..")
    input()
    #----------------------------------------------------------------------------------------
    #El croupier tiene que seguir sacando cartas hasta que su puntaje sea mayor o igual a 17.
    while croupier_puntaje < 17:
        print("croupier saca otra carta...")
        time.sleep(2)
        c_carta = random.choice(mazo)
        croupier_cartas.append(c_carta)
        mazo.remove(c_carta)
        croupier_puntaje += c_carta.carta_valor
        # Si la tercer carta es un 10 y antes tenia un as(11) y un 2, el as pasa a valer 1 y el total del puntaje sera 13.(10+1+2)
        c = 0
        while croupier_puntaje > 21 and c < len(croupier_cartas):
            if croupier_cartas[c].carta_valor == 11:
                croupier_cartas[c].carta_valor = 1
                croupier_puntaje -= 10
                c += 1
            else:
                c += 1
        time.sleep(1)
        verCartasyPuntos(croupier_cartas,False,croupier_puntaje)  
        time.sleep(1)
        # Si en la ronda del croupier,intentando superar los 17 puntos, este se pasa a 21, pierde.
        if croupier_puntaje > 21:
            print("Croupier supero los 21 puntos!")        
            print(nombre," Ganaste! Felicitaciones!")
            otrapartida()
        # Se evalua nuevamente si el croupier logro los 17 puntos, si no, se repite el proceso.
    # PARTE FINAL --- Una vez que el crupier tiene 17 o mas puntos, se evalua el puntaje de ambos y se obtiene el ganador.
    print("Eligiendo Ganador")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".\n")
    time.sleep(1)
    if croupier_puntaje == 21:
        print("Croupier tiene BLACKJACK!")
        print(nombre,"Perdiste, Mucha suerte la proxima!")
        otrapartida()
    elif croupier_puntaje == jugador_puntaje:
        print("Empate!!!!")
        otrapartida()
    elif croupier_puntaje > jugador_puntaje:
        print("Croupier supero tu puntaje!")
        print(nombre,"Perdiste, Mucha suerte la proxima!")
        otrapartida()   
    else:
        print(nombre," Ganaste! Felicitaciones!")
        otrapartida()
#----------------------------------------------------------------------------------------
#creo una funcion para que el usuario tenga la opcion de volver a jugar antes de salir.
def otrapartida():
    print("Desea jugar otra partida? (S/N)")
    respuesta = input("Opcion ingresada: ")
    while respuesta=="" or (respuesta.upper() != 'S' and respuesta.upper() != 'N'):
        print("Usted a ingresado una opcion incorrecta, solo puede ingresar las siguientes opciones:"
              "\nS-para volver a jugar"
              "\nN-para salir")
        respuesta = input("Opcion ingresada: ")
    if respuesta.upper() == 'S':
        time.sleep(2)
        blackjack(mazo)
    else:
        print("Gracias por jugar!")
        quit()
#----------------------------------------------------------------------------------------
if __name__ == '__main__':
    palos = "♥♦♣♠"
    cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cartas_valores = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    mazo = []
    for palo in palos:
        for carta in cartas:
            mazo.append(Cartas(palo, carta, cartas_valores[carta]))
    print('\033[1m'+"Bienvenido a Blackjack!"+'\033[0m')
    nombre = input("Ingresa tu nombre: ")
    while nombre == "":
        print("No puedes dejar el nombre vacío.")
        nombre = input("Ingresa tu nombre: ")
    print("Elija una opción para comenzar:"
        "\n1-Iniciar Juego"
        "\n2-Ver Reglas")
    opciones = input("Opcion ingresada: ")
    while (opciones != "1" and opciones != "2"):
        print("Usted a ingresado una opcion incorrecta, solo puede ingresar las siguientes opciones:"
                "\n1-Iniciar Juego"
                "\n2-Ver Reglas")
        opciones = input("Opcion ingresada: ")
    if opciones == "1":
        time.sleep(2)
        blackjack(mazo)
    elif opciones == "2":
        verReglas()
        blackjack(mazo)
#----------------------------------------------------------------------------------------


