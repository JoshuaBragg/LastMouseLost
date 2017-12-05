from random import randint as rand
from time import sleep as slp
from math import floor as fl

TIME_DELAY = 0

class Game():
	def __init__(self):
		self.b = [['o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o']]
	
	def update_b(self, r, a):
		i = 0
		while i < len(self.b[r]) and a > 0:
			if self.b[r][i] == 'o':
				self.b[r][i] = 'x'
				a -= 1
			i += 1
	
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
		
		#print ('0\t        ' + str(self.b[0]))
		#print ('1\t   ' + str(self.b[1]))
		#print ('2\t' + str(self.b[2]))
		#print ('3\t' + str(self.b[3]))
		#print ('4\t   ' + str(self.b[4]))
		#print ('5\t        ' + str(self.b[5]))
		
		#for i in self.b:
		#	print (i)
			
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
		return l
		#return self.b[:]

class Human_p():
	def move(self):
		r, a = (int(input('Row: ')), int(input('Amount: ')))
		return (r, a)
		
class Random_p():
	def __init__(self, g):
		self.g = g
		
	def move(self):
		r = rand(0,5)
		while self.g.row_empty(r):
			r = rand(0,5)
		return (r, rand(1,6))
		
class Smart_p():
	def __init__(self, g, d):
		self.g = g
		if d > 5:
			d = 5
		self.d = d
		
	def move(self):
		return self._game_host()
		
	def _game_host(self):
		ng = Game()
		trial_num = [5, 10, 25, 50, 100, 150]
		q = 0
		res = {}
		while q < trial_num[self.d]:
			ng.b = self.g.dupe()
			rand_p = Random_p(ng)
			out = self._trials(rand_p)
			if out[0] not in res:
				res[out[0]] = out[1]
			q += 1
		return res[min(res)]
			
	def _trials(self, rp):
		mv = rp.move()
		rp.g.update_b(mv[0], mv[1])
		mv_num = 0
		while not rp.g.g_o():
			cm = rp.move()
			rp.g.update_b(cm[0], cm[1])
			mv_num += 1
		return (mv_num, mv)
		
if __name__ == '__main__':
	g = Game()
	pn = True
	pl = [Human_p(), Random_p(g)]
	while not g.g_o():
		g.draw()
		if pn:
			print ('\nP1')
			r, a = pl[0].move()
		else:
			print ('\nP2')
			slp(TIME_DELAY)
			r, a = pl[1].move()
			
		print ('\n---------------------------------------------------\n')
		g.update_b(r, a)
		pn = not pn
	
	if pn:
		print ('Player 1 Wins')
	else:
		print ('Player 2 Wins')
