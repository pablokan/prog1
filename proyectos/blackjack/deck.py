import random
from super_foo import superFoo

superFoo('pablo')

def getDeck():
    
    suits_symbols = ['♠', '♦', '♥', '♣']
    SPADES = '\u2660'  # '♠'
    CLUBS = '\u2663' #  '♣'
    HEARTS = '\u2665'  # '♥'
    DIAMONDS = '\u2666'  # '♦'.
    
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add the numbered cards.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # Add the face and ace cards.
    random.shuffle(deck)
    print(SPADES, HEARTS, CLUBS, DIAMONDS)
    return deck

#print(getDeck())





