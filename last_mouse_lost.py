from random import randint as rand
from time import sleep as slp
from board import Board
from smart_player import Node, MinMax, goodDepth
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

	def dupe(self):
		return self.b.dupe()

	def run_game(self, num_h, num_r, num_s):
		cur_p = 1
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
				print(f'\n{playr} {l.index(playr)} made move ({plm[0]}, {plm[1]})\n\n---------------------------------------------------\n')
				if self.game_over():
					print(f'\n\n{playr} {l.index(playr)} Lost')
					break

if __name__ == '__main__':
	g = Game()
	g.run_game(1, 0, 1)



















