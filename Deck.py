'''
the Deck class holds all 52 cards in a deck and scrables their order
'''
import random
from Card import Card
class Deck():

    def __init__(self):
        self.suits = ('hearts', 'diamonds', 'spades', 'clubs')
        self.ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'jack', 'king', 'queen', 'ace')
        self.cards = []

        # makes a list of all cards, four of each rank 
        for s in self.suits:
            for r in self.ranks:
                new_card = Card(s,r)
                self.cards.append(new_card)
                
        # shuffle the deck
        random.shuffle(self.cards)
    

