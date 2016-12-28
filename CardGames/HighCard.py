from Cards.CardDeck import CardDeck
from Players.Player import Player
####################################################################################################
# file  : HighCard.py
# author: Chris Kreider
# date  : 12/27/16
# notes : program to play "high" card between two players
####################################################################################################

#display some generic output
print("card deck test program")
print("the game is high card")

#create the players
player_one = Player()
player_two = Player("Chris")

#lets echo who is playing
print("The players are as follows")
print(player_one)
print(player_two)

#get a new deck of cards and shuffle them
card_deck=CardDeck()
card_deck.shufle()

#deal a card to the players
player_one.take_card(card_deck.deal_card())
player_two.take_card(card_deck.deal_card())

#check and display the status after dealing cards
print("The players have each been dealt a card - their values are")
print(player_one)
print(player_two)

#decide who won
if(player_one.show_card()>player_two.show_card()):
    print("the winner is "+player_one.get_name())
else:
    print("the winner is " + player_two.get_name())


