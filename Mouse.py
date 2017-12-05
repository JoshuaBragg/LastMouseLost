class Game():
	def __init__(self):
		self.b = [['o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o', 'o'],['o', 'o', 'o', 'o', 'o'],['o', 'o', 'o']]
	
	def move(self, r, a):
		i = 0
		while i < len(self.b[r]) and a > 0:
			if self.b[r][i] == 'o':
				self.b[r][i] = 'x'
				a -= 1
			i += 1

	def draw(self):
		print ('0\t        ' + str(self.b[0]))
		print ('1\t   ' + str(self.b[1]))
		print ('2\t' + str(self.b[2]))
		print ('3\t' + str(self.b[3]))
		print ('4\t   ' + str(self.b[4]))
		print ('5\t        ' + str(self.b[5]))
		#for i in self.b:
		#	print (i)
			
	def g_o(self):
		for i in self.b:
			for c in i:
				if c == 'o':
					return False
		return True
		
if __name__ == '__main__':
	g = Game()
	pn = True
	while not g.g_o():
		g.draw()
		
		if pn:
			print ('\nP1')
		else:
			print ('\nP2')
		
		g.move(int(input('r')), int(input('a')))
		pn = not pn
	
	if pn:
		print ('Player 1 Wins')
	else:
		print ('Player 2 Wins')
