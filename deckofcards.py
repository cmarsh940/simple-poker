#52 cards
#shuffle and deal
# create player with name and hand
# player should be able to draw a card from deck and discard their hand.

import Deck from deck


class Poker(object):
	#initialze
	def __init__(self, id, card, num_players):
		self.id = id
		self.card = card
		self.suite =  suite
		self.num_players = num_players



	def displayinfo(self):
		return "id: {} card: {} suite: {} num_players: {}".format(
		self.id,	    
		self.card,
		self.suite,
		self.num_players  
		)







# print Poker(52, 5)
# print deck
player1 = Player(1)
player2 = Player(2)
print Deck