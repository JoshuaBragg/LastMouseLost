from random import randint as rand
import collections as col


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
		return (r, rand(1, self.board.spot_avail(r)))

	def move(self):
		cur_b = col.Counter(self.board.num_row())
		if cur_b in [{0: 2, 1: 4}, {0: 2, 1: 3, 2: 1}, {0: 2, 1: 3, 3: 1}, {0: 2, 1: 3, 4: 1}, {0: 2, 1: 3, 5: 1}, {0: 2, 1: 3, 6: 1}, {1: 6}, {1: 5, 2: 1}, {1: 5, 3: 1}, {1: 5, 4: 1}, {1: 5, 5: 1}, {1: 5, 6: 1}, {0: 4, 1: 2}, {0: 4, 1: 1, 2: 1}, {0: 4, 1: 1, 3: 1}, {0: 4, 1: 1, 4: 1}, {0: 4, 1: 1, 5: 1}, {0: 4, 1: 1, 6: 1}]:
			m = 0
			r = 0
			for i in range(len(self.board)):
				if self.board.spot_avail(i) > m:
					m = self.board.spot_avail(i)
					r = i
			return (r, m)
		elif cur_b in [{0: 1, 1: 4, 2: 1}, {0: 1, 1: 4, 3: 1}, {0: 1, 1: 4, 4: 1}, {0: 1, 1: 4, 5: 1}, {0: 1, 1: 4, 6: 1}, {0: 3, 1: 2, 2: 1}, {0: 3, 1: 2, 3: 1}, {0: 3, 1: 2, 4: 1}, {0: 3, 1: 2, 5: 1}, {0: 3, 1: 2, 6: 1}, {0: 5, 2: 1}, {0: 5, 3: 1}, {0: 5, 4: 1}, {0: 5, 5: 1}, {0: 5, 6: 1}]:
			m = 0
			r = 0
			for i in range(len(self.board)):
				if self.board.spot_avail(i) > m:
					m = self.board.spot_avail(i)
					r = i
			return (r, m - 1)
		elif cur_b == {0: 1, 1: 5}:
			for i in range(len(self.board)):
				if self.board.spot_avail(i) == 1:
					return (i, 1)
		else:
			if self.board.b[0] != self.board.b[5]:
				return self.board.diff(0, 5)
			if self.board.b[1] != self.board.b[4]:
				return self.board.diff(1, 4)
			if self.board.b[2] != self.board.b[3]:
				return self.board.diff(2, 3)
			else:
				return self._rmove()

	def __str__(self):
		return 'Smart Player'
