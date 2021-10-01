from random import shuffle

class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        
    def recibirCarta(self, carta):
        self.mano.append(carta)
        
    def verMano(self, dealer_start=True):
        pass

    def calcularMano(self):
        pass

class Blackjack():
    def __init__(self):
        palos = ("Pique", "Corazón", "Diamante", "Trébol")
        valores = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
        self.mazo = [(palo, valor) for valor in valores for palo in palos]
        shuffle(self.mazo)

        nombre = input("Nombre: ")
        jugador = Jugador(nombre)
        dealer = Jugador("Dealer")
        jugador.recibirCarta(self.darCarta())
        jugador

    def darCarta(self):    
        return self.mazo.pop()
    
                
juego = Blackjack()
