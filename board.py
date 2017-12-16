from math import floor as fl
import collections as col

class Board():
	def __init__(self):
		self.b = [['o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o']]
		
	def update_b(self, r, a):
		i = 0
		while i < len(self.b[r]) and a > 0:
			if self.b[r][i] == 'o':
				self.b[r][i] = 'x'
				a -= 1
			i += 1
			
	def spot_avail(self, r):
		s = 0
		for i in self.b[r]:
			if i == 'o':
				s += 1
		return s
			
	def row_empty(self, r):
		for i in self.b[r]:
			if i == 'o':
				return False
		return True
		
	def draw(self):
		for i in range(len(self.b)):
			print(f'{i}' + ' '*(fl((i-2.5)**2)+4), end='')
			for c in self.b[i]:
				print (c, end='   ')
			print()
			
	def g_o(self):
		for i in self.b:
			for c in i:
				if c == 'o':
					return False
		return True
		
	def dupe(self):
		l = [[],[],[],[],[],[]]
		for i in range(len(self.b)):
			for c in self.b[i]:
				l[i].append(c)
		b = Board()
		b.b = l
		return b
		
	def one_left(self):
		am = 0
		for r in range(len(self.b)):
			for i in self.b[r]:
				if i == 'o':
					am += 1
		return am == 1
		
	def num_row(self):
		l = []
		for i in range(len(self.b)):
			s = 0
			for c in self.b[i]:
				if c == 'o':
					s += 1
			l.append(s)
		return l
		
	def win_board(self):
		win_b = [{0:4,3:2}, {0:4,2:2}, {0:3,1:1,2:1,3:1}, {0:3,1:3}, {0:1,1:5}, {0:4,4:2}, {0:2,1:2,3:2}, {0:2,1:2,2:2}]  #, {0:2,6:1,5:2,3:1}
		cb = col.Counter(self.num_row())
		if cb not in win_b:
			return False
		return True
	
	def __eq__(self, b):
		if not ((self.b[0] == b.b[0] and self.b[5] == b.b[5]) or (self.b[0] == b.b[5] and self.b[5] == b.b[0])):
			return False
		if not ((self.b[1] == b.b[1] and self.b[4] == b.b[4]) or (self.b[1] == b.b[4] and self.b[4] == b.b[1])):
			return False
		if not ((self.b[2] == b.b[2] and self.b[3] == b.b[3]) or (self.b[2] == b.b[3] and self.b[3] == b.b[2])):
			return False
		return True
