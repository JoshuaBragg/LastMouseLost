from math import floor as fl

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
