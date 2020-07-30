'''
the Hand class deals with each player's cards and the sum of their cards
'''
from Card import Card

class Hand():
    
    def __init__(self):
        self.sum = 0
        self.aces = 0
        self.cards = []
        self.bust = False
        self.values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,
                  'eight':8,'nine':9,'ten':10,'jack':10,'king':10,'queen':10, 'ace':11}
    
    # add a card to the hand 
    def add(self, card):
        self.cards.append(card)
        if (card.rank == 'ace'):
            self.aces += 1
        self.sum += self.values[card.rank]
        self.busted()
        # if the hand is a bust check to see if it was a 'soft' bust 
        if (self.bust):
            x = self.aces
            while x > 0:
                if ((self.sum > 21)):
                    self.sum -= 10
                    self.aces -= 1
                x -= 1
                
        
    # determine if the sum of the hand is greater than 21        
    def busted(self):
        if self.sum > 21:
            self.bust = True
        else:
            self.bust = False
    # handle the player hitting
    def hit(self):
        resp = ""
        while resp == "":
            resp = input("Hit? y/n--> ")
            if resp =="y":
                return True
            elif resp == "n":
                return False
            else:
                resp = ""
        
    def dealer_start(self):
        print(self.cards[0])
        
    def player_start(self):
        print(str(self.cards[0]) + ' & ' + str(self.cards[1]))
    
    
    
        
