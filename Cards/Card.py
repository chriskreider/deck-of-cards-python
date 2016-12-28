####################################################################################################
# file  : Card.py
# author: Chris Kreider
# date  : 12/27/16
# notes : represents a card that is part of a deck of cards
####################################################################################################


####################################################################################################
# class: Card
# notes: single card from a deck of Cards
####################################################################################################
class Card(object):
    suit          = "X"
    suit_ordinal  = -1
    value         = -1
    value_ordinal = -1
    deck_id       = -1

    # ------------------------------------------------------------------------------
    # method: __init__
    # params:
    #   self:
    #   suit: the cards suit
    #   value: the cards value
    # notes :
    # ------------------------------------------------------------------------------
    def __init__(self, suit, suit_ordinal, value, value_ordinal, deck_id):
        self.suit          = suit
        self.suit_ordinal  = suit_ordinal
        self.value         = value
        self.value_ordinal = value_ordinal
        self.deck_id       = deck_id
        return

    # ------------------------------------------------------------------------------
    # method: __str__
    # params:
    #   self:
    # notes : returns a string version of the suit+value of the card
    # ------------------------------------------------------------------------------
    def __str__(self):
        return self.value+" of "+self.suit +"(from deck "+self.deck_id.__str__()+")"

    # ------------------------------------------------------------------------------
    # method: __sgt__
    # params:
    #   self:
    # notes : returns if the current card is greater than (gt) the provided card
    # ------------------------------------------------------------------------------
    def __gt__(self, compare_to):
        if(self.value_ordinal>compare_to.value_ordinal):
            return True
        elif(self.value_ordinal==compare_to.value_ordinal):
            if(self.suite_ordinal>compare_to.suit_ordinal):
                return True
            else:
                return False
        return