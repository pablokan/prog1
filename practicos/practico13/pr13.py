from random import shuffle


class Jugador:
    def __init__(self, name):
        self.name = name
        self.hand = []

    # take in a tuple and append it to the hand
    def addCard(self, card):
        self.hand.append(card)

    # if not dealer's turn, then only show one of his cards, otherwise show all cards
    def showHand(self, dealer_start=True):
        print("\n{}".format(self.name))
        print("===========")

        for i in range(len(self.hand)):
            if self.name == "Dealer" and i == 0 and dealer_start:
                print("- of -")  # hide first card
            else:
                card = self.hand[i]
                print("{} of {}".format(card[0], card[1]))
        print("Total = {}".format(self.calcHand(dealer_start)))

    # if not dealer's turn then only give back total of second card
    def calcHand(self, dealer_start=True):
        total = 0
        aces = 0  # calculate aces afterwards
        card_values = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11,
        }

        if self.name == "Dealer" and dealer_start:
            card = self.hand[1]
            return card_values[card[0]]

        for card in self.hand:
            if card[0] == "A":
                aces += 1
            else:
                total += card_values[card[0]]

        for i in range(aces):
            if total + 11 > 21:
                total += 1
            else:
                total += 11

        return total


class Blackjack:
    def __init__(self):
        self.deck = []  # set to an empty list
        self.suits = ("Spades", "Hearts", "Diamonds", "Clubs")
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")

    # create a method that creates a deck of 52 cards, each card should be a tuple with a value and suit
    def makeDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))  # ex: (7, "Hearts")

    # method to pop a card from deck using a random index value
    def pullCard(self):
        return self.deck.pop(randint(0, len(self.deck) - 1))


# create a class for the dealer and Jugador objects

game = Blackjack()
game.makeDeck()

name = input("What is your name?")
jugador = Jugador(name)
dealer = Jugador("Dealer")

# add two cards to the dealer and Jugador hand
for i in range(2):
    jugador.addCard(game.pullCard())
    dealer.addCard(game.pullCard())

# show both hands using method
Jugador.showHand()
dealer.showHand()

Jugador_bust = False

while input("Would you like to stay or hit?").lower() != "stay":

    # pull card and put into Jugador's hand
    Jugador.addCard(game.pullCard())

    # show both hands using method
    Jugador.showHand()
    dealer.showHand()

    # check if over 21
    if Jugador.calcHand() > 21:
        Jugador_bust = True
        break

# handling the dealer's turn, only run if Jugador didn't bust
dealer_bust = False

if not Jugador_bust:
    while dealer.calcHand(False) < 17:
        # pull card and put into Jugador's hand
        dealer.addCard(game.pullCard())

        # check if over 21
        if dealer.calcHand(False) > 21:
            dealer_bust = True
            break

# show both hands using method
Jugador.showHand()
dealer.showHand(False)

# calculate a winner
if Jugador_bust:
    print("You busted, better luck next time!")
elif dealer_bust:
    print("The dealer busted, you win!")
elif dealer.calcHand(False) > Jugador.calcHand():
    print("Dealer has higher cards, you lose!")
elif dealer.calcHand(False) < Jugador.calcHand():
    print("You beat the dealer! Congrats!")
else:
    print("You pushed, no one wins!")
