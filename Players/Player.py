####################################################################################################
# file  : Player.py
# author: Chris Kreider
# date  : 12/28/16
# notes : player capable of being dealt cards as part of the card games python exercise
#
#
####################################################################################################




####################################################################################################
# class: Player
# notes: represents a player capable of being dealt cards
####################################################################################################
class Player(object):
    player_name      = ""
    anon_player_count= 0
    cards_in_hand    = []

    #------------------------------------------------------------------------------
    # method: __self__
    # params:
    #   self:
    #   name: <optional> players name
    # notes : default ctor creates a named or numbered (anonymous) player based on
    #         either the provided name, or the total number of anonymous
    #         player objects instantated (e.g. player 1, player 2, etc)
    # -----------------------------------------------------------------------------
    def __init__(self, name=""):
        # initialize some variables as self
        self.cards_in_hand = []
        # decide if a real name was provided to decide how this instances name
        # variable will be set
        if name=="":
            Player.anon_player_count += 1
            # if a name is not provided, use a numbered player to create the name
            self.player_name = "Player " + Player.anon_player_count.__str__()
        else:
            #otherwise, use the provided name
            self.player_name=name
        return

    # ------------------------------------------------------------------------------
    # method: __str__
    # params:
    #   self:
    # notes : generates a string name for the player along with other info about
    #         the player in a semi formatted manner
    # -----------------------------------------------------------------------------
    def __str__(self):
        player_string = ""
        player_string += "--------------------------------------------------------------------------------\n"
        player_string += "name      : "+self.player_name+"\n"
        player_string += "card count: "+ len(self.cards_in_hand).__str__()+"\n"
        if len(self.cards_in_hand)>0:
            for card in self.cards_in_hand:
                player_string+= "          : "+card.__str__()+"\n"

        player_string += "--------------------------------------------------------------------------------\n"
        return   player_string

    # ------------------------------------------------------------------------------
    # method: take_card
    # params:
    #   self:
    #   card: a card to add to a players hand
    # notes : generates a string name for the player
    # -----------------------------------------------------------------------------
    def take_card(self, card):
        self.cards_in_hand.append(card)
        return

    # ------------------------------------------------------------------------------
    # method: get_name
    # params:
    #   self:
    # notes : returns the player name assigned to the player instance
    # -----------------------------------------------------------------------------
    def get_name(self):
        return self.player_name

    # ------------------------------------------------------------------------------
    # method: show_card
    # params:
    #   self:
    # notes : shows the first card in the players pile
    # -----------------------------------------------------------------------------
    def show_card(self):
        return self.cards_in_hand[0]
