from board import Board
from player import HumanPlayer, RandomPlayer, SmartPlayer


class Game:
	def __init__(self):
		self.b = Board()

	def make_move(self, r, a):
		self.b.update_b(r, a)

	def draw_board(self):
		self.b.draw()

	def game_over(self):
		return self.b.g_o()

	def run_game(self, num_h, num_r, num_s):
		t = 0
		l = []
		for i in range(num_h):
			l.append(HumanPlayer(self.b))
			t += 2
		for i in range(num_r):
			l.append(RandomPlayer(self.b))
			t += 2
		for i in range(num_s):
			l.append(SmartPlayer(self.b, -1 + t))
			t += 2
		while not self.game_over():
			for playr in l:
				self.draw_board()
				plm = playr.move()
				self.make_move(plm[0], plm[1])
				print('\n' + str(playr) + ' ' + str(l.index(playr)) + ' made move (' + str(plm[0]) + ', ' + str(plm[1]) + ')\n\n---------------------------------------------------\n')
				if self.game_over():
					print('\n\n' + str(playr) + ' ' + str(l.index(playr)) + ' Lost')
					return l.index(playr)


if __name__ == '__main__':
	g = Game()
	g.run_game(1, 0, 1)
