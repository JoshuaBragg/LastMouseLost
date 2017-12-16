from random import randint as rand
from time import sleep as slp
from board import Board
from smp1 import Node, MinMax, goodDepth
from sys import maxsize

TIME_DELAY = 0

class Game():
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
				
if __name__ == '__main__':
	g = Game()
	l = [['x', 'x', 'x'],['x', 'x', 'x', 'x', 'o'],['o', 'o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o']]#[['o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o']]
	bord = Board()
	bord.b = l
	g.b = bord
	cur_p = 1
	depth = goodDepth(bord)
	while not g.game_over():
		g.draw_board()
		pr = int(input('Row: '))
		pa = int(input('Amount: '))
		while bord.row_empty(pr) or pa <= 0 or pr < 0 or pr > 5:
			print('Invalid move')
			pr = int(input('Row: '))
			pa = int(input('Amount: '))
		g.make_move(pr, pa)
		if not g.game_over():
			print('-------------------------------------------------------')
			g.draw_board()
			depth = goodDepth(bord)
			cur_p *= -1
			node = Node(depth, -1*cur_p, g.b)
			
			bC = (0, -1)
			bV = -1 * cur_p * maxsize
			for child in node.children:
				i_val = MinMax(child, depth, -1 * cur_p)
				if (abs(maxsize * cur_p - i_val) < abs(maxsize * cur_p - bV)):
					bV = i_val
					bC = child.move
			if bC == (0, -1):
				h = rmove(g.b)
				g.make_move(h[0], h[1])
				bC = h
			else:
				g.make_move(bC[0], bC[1])
			print(f'Computer made move {bC}')
		else:
			print('-------------------------------------------------------')
			print('-------------------------------------------------------')
			g.draw_board()
			print(f'\n\tComp won')
			break
		if g.game_over():
			print('-------------------------------------------------------')
			print('-------------------------------------------------------')
			g.draw_board()
			print(f'\n\tHuman won')
			break
		cur_p *= -1
		print('-------------------------------------------------------')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
