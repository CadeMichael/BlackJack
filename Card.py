'''
the Card class defines an individual card with a suit and rank
'''
class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    #print the card in a way the user can understand
    def __str__(self):
        return (self.rank + ' of ' + self.suit)
