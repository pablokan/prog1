from random import shuffle

palos = ("Pique", "Corazón", "Diamante", "Trébol")
valores = ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")
mazo = [(palo, valor) for palo in palos for valor in valores]
shuffle(mazo)
print(mazo)

def darCarta():
    return mazo.pop()

carta1 = darCarta()
print(carta1)
print(mazo)

carta2 = darCarta()
print(carta2)
print(mazo)
