'''
game encorporates all the classes and uses them to run the blackjack game
'''

from Hand import Hand
from Deck import Deck
from Balance import Balance

game_on = True
current = 0
balance = Balance()

# once the game is over ask if the player wants to play again
def play():
    answer = ""
    # wait for an answer
    while answer == "":
        answer = input("\n do you want to play again? y/n--> ")
        if answer =="y":
            return True
        elif answer == "n":
            return False
        else:
            answer = ""

# at the start of each game reset the global variables and give the player/ dealer their cards
def setup_game():
    print("balance: " + str(balance))
    # take the player's bet
    balance.make_bet()
    # set variables
    global current
    current = 0
    global deck
    deck = Deck()
    global dealer_hand
    dealer_hand = Hand()
    global player_hand
    player_hand = Hand()
    # give initial cards
    player_hand.add(deck.cards[current])
    current += 1
    dealer_hand.add(deck.cards[current])
    current += 1
    player_hand.add(deck.cards[current])
    current += 1
    dealer_hand.add(deck.cards[current])
    current += 1
    print("dealer: ")
    dealer_hand.dealer_start()
    print("your hand: ")
    player_hand.player_start()

# handle the automatic hitting of the dealer, must hit if under 16
def dealer_hit(current):
    while (dealer_hand.sum < 16):
        dealer_hand.add(deck.cards[current])
        print(deck.cards[current])
        print("sum: " + str(dealer_hand.sum))
        current += 1
        # dealer busted
        if (dealer_hand.sum > 21):
            break

# show if the dealer or the player has won
def verdict(dealer, player):
    if (dealer > player and dealer < 22):
        return "dealer"
    return "player"

# while the user wants to play
while (game_on):
    # initialize the game
    setup_game()
    
    # allow the player to hit as much as they want
    while(player_hand.hit()):
        player_hand.add(deck.cards[current])
        print(deck.cards[current])
        print(player_hand.sum)
        current += 1
        player_hand.busted()
        if (player_hand.bust):
            print("busted")
            game_on = play()
            break
    
    # if the player has not busted allow the dealer to hit
    if (player_hand.bust == False):
        print("dealer's Cards: ")
        for x in dealer_hand.cards:
            print(x)
        dealer_hit(current)
        # determine the winner
        winner = verdict(dealer_hand.sum, player_hand.sum)
        if (winner == "dealer"):
            print("you lose")
            print(str(balance.balance))
        else:
            print("you win")
            # increase the balance
            balance.win()
        # check if the user wants to play again
        game_on = play()
        
    
    
    
        
