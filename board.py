from math import floor as fl


class Board:
	def __init__(self):
		self.b = [['o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o'],
					['o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o']]

	def update_b(self, r, a):
		i = 0
		while i < len(self.b[r]) and a > 0:
			if self.b[r][i] == 'o':
				self.b[r][i] = 'x'
				a -= 1
			i += 1

	def spot_avail(self, r):
		s = 0
		for i in range(len(self.b[r])-1, -1, -1):
			if self.b[r][i] == 'x':
				break
			s += 1
		return s

	def row_empty(self, r):
		for i in range(len(self.b[r])-1, -1, -1):
			if self.b[r][i] == 'o':
				return False
		return True

	def draw(self):
		for i in range(len(self.b)):
			print(f'{i}' + ' '*(int(fl((i-2.5)**2)+4)), end='')
			for c in self.b[i]:
				print(c, end='   ')
			print()

	def g_o(self):
		for i in self.b:
			for c in range(len(i)-1, -1, -1):
				if i[c] == 'o':
					return False
				else:
					break
		return True

	def __len__(self):
		return len(self.b)

	def num_row(self):
		temp_l = []
		for i in range(len(self.b)):
			s = 0
			for c in range(len(self.b[i])-1, -1, -1):
				if self.b[i][c] == 'o':
					s += 1
				else:
					break
			temp_l.append(s)
		return temp_l

	def diff(self, r1, r2):
		r10 = 0
		r20 = 0
		for i in range(0, len(self.b[r1])):
			if self.b[r1][i] == 'o':
				r10 += 1
			if self.b[r2][i] == 'o':
				r20 += 1
		if r10 > r20:
			return (r1, r10 - r20)
		else:
			return (r2, r20 - r10)
