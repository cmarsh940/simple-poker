import random
from card import card

class Deck(object):
	def build(self):
		self.cards = []
		self._build()

	def _build(self):
		suite = ['c', 'd', 'h', 's']
		ranks = ['2', '3', '4', '5', '6', '7', '8', '9','T', 'J', 'Q', 'K', 'A']

		
		for rank in ranks:
			for suite in suites:
				card = Card(rank, suite)

				deck.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

	def deal(self, player):
		card = self.cards.pop(0)

		player.addCard(card)

	def display(self):
        for card in self.cards:
            print card