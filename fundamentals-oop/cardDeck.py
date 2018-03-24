class Deck(object):
    def __init__(self):
        self.cards = []
    def addCard(self, card):
        self.cards.append(card)
        return self
    def deal(self, cardlist):
        print self.cards[0]
        return self
    def shuffle(self, cardlist):


        return self

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

suits = ['hearts','diamonds','clubs','spades']
values = ['ace',2,3,4,5,6,7,8,9,'jack','queen', 'king']


