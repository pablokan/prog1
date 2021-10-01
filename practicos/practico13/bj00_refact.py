from random import shuffle

class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        
    def recibirCarta(self, carta):
        self.mano.append(carta)
        
    def verMano(self):
        print(self.mano)
        vMano = [e[1] for e in self.mano]

        for i, e in enumerate(vMano):
            if e == "J" or e == "Q" or e == "K":
                vMano[i] = 10
            elif e == "A":
                vMano[i] = 1
        print(vMano)
        total1 = sum(vMano)
        total2 = 0
        cartel = f"Total: {total1}"
        if vMano.count(1) != 0 and total1 + 10 < 22:
            total2 = total1 + 10
            cartel += f" o {total2}"
        if total1 == 21 or total2 == 21:
            cartel = "Blackjack!"
        print(cartel)

    
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
        jugador.recibirCarta(self.darCarta())
        jugador.verMano()

    def darCarta(self):    
        return self.mazo.pop()
    
                
juego = Blackjack()
