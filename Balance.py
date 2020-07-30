'''
the Balance class holds the amount of money the player has
'''
class Balance():
    
    # the player starts with 100 dollars at the start of each new game
    def __init__(self):
        self.balance = 100
        self.bet = 0
    
    # prints the balance in an understandable format
    def __str__(self):
        return(str(self.balance) + ' dollars')
    
    # take an input which represents the bet before the cards are dealt
    def make_bet(self):
        bet = int(input("starting bet: "))
        # the bet is only accepted if there are enough funds for it
        while(bet > self.balance):
            print('not enough funds')
            bet = int (input("starting bet: "))
        self.balance -= bet
        self.bet = bet
        
    # if the player wins they earn back what they bet
    def win(self):
        self.balance += 2*self.bet
        print(self)
        
    
