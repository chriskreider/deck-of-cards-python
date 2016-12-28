from Card import Card
import random
####################################################################################################
# file  : CardDeck.py
# author: Chris Kreider
# date  : 12/27/16
# notes : Sample Project to learn python around the concept of a class for a deck of cards
#         and then creating different classes that use this class to create games such as
#         high card (simple) or poker (more complex)
####################################################################################################



####################################################################################################
# class: CardDeck
# notes: Represents a deck of cards used in card games
####################################################################################################
class CardDeck(object):
    suits  = {"Clubs":1, "Diamonds":2, "Hearts":3, "Spades":4}#assumes alphabetical high suit as in bridge
    # NOTE: ace assumed high - may add a method later to to allow aces to bigh high/low etc
    values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}
    cards  = []
    # ------------------------------------------------------------------------------
    # method: __init__
    # params:
    #   self:
    # notes : default ctor
    # ------------------------------------------------------------------------------
    def __init__(self):
        print("card deck initializing")
        #create all the cards by combination of suits and values
        for suit, suit_ordinal in self.suits.iteritems():
            for value, value_ordinal in self.values.iteritems():
                self.cards.append(Card(suit,suit_ordinal,value, value_ordinal, id(self)))
        return


    #------------------------------------------------------------------------------
    # method: shuffle
    # params:
    #   self:
    # notes : shuffles the deck which starts in a default ordered state
    # ------------------------------------------------------------------------------
    def shufle(self):
        random.shuffle(self.cards)
        return


    # ------------------------------------------------------------------------------
    # method: deal_card
    # params:
    #   self:
    # notes : deals a card from the deck
    # ------------------------------------------------------------------------------
    def deal_card(self):
        return self.cards.pop()


    # ------------------------------------------------------------------------------
    # method: __str__
    # params:
    #   self:
    # notes : displays the contents of the deck of cards in the order they exist
    #         in the deck
    # ------------------------------------------------------------------------------
    def __str__(self):
        deck_contents=""
        # display the cards that were added
        for card in self.cards:
            deck_contents+=card.__str__()+"\n"
        return deck_contents


