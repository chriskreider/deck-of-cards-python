from Players.Player import Player
####################################################################################################
# file  : CardGame.py
# author: Chris Kreider
# date  : 12/28/16
# notes : Meant to contain an abstract superclass with high level details that are consistent
#         across card games such as players and decks of cards.
####################################################################################################




####################################################################################################
# class: CardGame
# notes: represents a high level card game (meant to be an abstract superclass)
####################################################################################################
class CardGame(object):
    name_of_game= ""
    players     = []
    decks       = []


	#------------------------------------------------------------------------------
    # method:__init__
    # params:
    #   self:
    #   name_of_game: what is the name of the underlying card game that this class
    #                 is holding information about?
    # notes : initializes features of a basic card game
	# -----------------------------------------------------------------------------
    def __init__(self, name_of_game=""):
        #add a deck of cards


        #set the member variables based on what was provided
        self.name_of_game=name_of_game
        return


    # ------------------------------------------------------------------------------
    # method:add_player
    # params:
    #   self:
    #   name:<optional> if player has a name, provide it here
    # notes : initializes features of a basic card game
    # -----------------------------------------------------------------------------
    def add_player(self, name):
        self.players.append(Player(name))
        return



