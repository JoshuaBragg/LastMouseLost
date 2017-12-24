from random import randint as rand
from smart_player import Node, min_max, good_depth
from sys import maxsize


class Player:
	def __init__(self, board):
		self.board = board

	def move(self):
		raise NotImplementedError


class RandomPlayer(Player):
	def move(self):
		r = rand(0, 5)
		while self.board.row_empty(r):
			r = rand(0, 5)
		return (r, rand(1, self.board.spot_avail(r)) + 1)

	def __str__(self):
		return 'Random Player'


class HumanPlayer(Player):
	def move(self):
		try:
			pr = int(input('Row: '))
			pa = int(input('Amount: '))
		except ValueError:
			pr = -1
			pa = -1
		while pr > 5 or self.board.row_empty(pr) or pa <= 0 or pr < 0:
			print('Invalid move')
			try:
				pr = int(input('Row: '))
				pa = int(input('Amount: '))
			except ValueError:
				pr = -1
				pa = -1
		return (pr, pa)

	def __str__(self):
		return 'Human Player'


class SmartPlayer(Player):
	def __init__(self, board, pn):
		Player.__init__(self, board)
		self.pn = pn

	def _rmove(self):
		r = rand(0, 5)
		while self.board.row_empty(r):
			r = rand(0, 5)
		return (r, rand(1, self.board.spot_avail(r)) + 1)

	def move(self):
		depth = good_depth(self.board)
		node = Node(depth, -1*self.pn, self.board)

		best_choice = (0, -1)
		best_val = -1 * self.pn * maxsize
		for child in node.children:
			i_val = min_max(child, depth, -1 * self.pn)
			if abs(maxsize * self.pn - i_val) < abs(maxsize * self.pn - best_val):
				best_val = i_val
				best_choice = child.move
			# if bV == self.pn*maxsize:
			# 	break
		if best_choice == (0, -1):
			h = self._rmove()
			best_choice = h
		return best_choice

	def __str__(self):
		return 'Smart Player'
