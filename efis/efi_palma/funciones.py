import time
from cartas import mostrar_cartas
#Creamos una funcion para ver las cartas del jugador o del croupier segun los parametros que le pasemos 
def verCartasyPuntos(cartas,oculta,puntaje,nombre="croupier"):
    print("Cartas de "+nombre+":")
    mostrar_cartas(cartas,oculta)
    print("Puntaje:",puntaje)
#Funcion que nos muestra de forma resumida las principales reglas del juego.  
def verReglas():
    print("\nReglas del juego:")
    print("El objetivo consiste en sumar un valor lo más próximo a 21 pero sin pasarse.")
    print("Se juega unicamente contra el croupier, el cual está obligado a pedir una carta",end=" ")
    print("siempre que su puntuación sume 16 o menos, y obligado a plantarse si suma 17 o más.")
    print("El jugador tiene la opción de pedir una carta o plantarse en cualquier momento!")
    print("Las cartas numéricas suman su valor,las figuras suman 10 y el As puede vale 11 o 1, segun convenga.",end=" ") 
    print("En el caso del crupier, los Ases valen 11 mientras no se pase de 21, y 1 en caso contrario.")
    time.sleep(1)
    input("\nPresione enter para continuar...y comenzar el juego.")
