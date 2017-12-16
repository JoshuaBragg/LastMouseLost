from sys import maxsize


class Node:
	def __init__(self, depth, pnum, board, move=(0, 0), val=0):
		self.depth = depth
		self.pnum = pnum
		self.board = board
		self.val = val
		self.move = move
		self.children = []
		self.create_children()

	def create_children(self):
		if self.depth < 0 or self.val != 0:
			return
		# This is much messier than before but cuts down tree size because of the symmetry of the board
		if self.board.b[0] == self.board.b[5]:
			if self.board.b[1] == self.board.b[4]:
				if self.board.b[2] == self.board.b[3]:
					for r in range(3):
						if not self.board.row_empty(r):
							for a in range(self.board.spot_avail(r)):
								tempb = self.board.dupe()
								tempb.update_b(r, a+1)
								self.children.append(Node(self.depth - 1, -1*self.pnum, tempb, (r, a+1), self.RealVal(self.board)))
				else:
					for r in range(4):
						if not self.board.row_empty(r):
							for a in range(self.board.spot_avail(r)):
								tempb = self.board.dupe()
								tempb.update_b(r, a+1)
								self.children.append(Node(self.depth - 1, -1*self.pnum, tempb, (r, a+1), self.RealVal(self.board)))
			else:
				if self.board.b[2] == self.board.b[3]:
					for r in [0, 1, 2, 4]:
						if not self.board.row_empty(r):
							for a in range(self.board.spot_avail(r)):
								tempb = self.board.dupe()
								tempb.update_b(r, a+1)
								self.children.append(Node(self.depth - 1, -1*self.pnum, tempb, (r, a+1), self.RealVal(self.board)))
				else:
					for r in [0, 1, 2, 3, 4]:
						if not self.board.row_empty(r):
							for a in range(self.board.spot_avail(r)):
								tempb = self.board.dupe()
								tempb.update_b(r, a+1)
								self.children.append(Node(self.depth - 1, -1*self.pnum, tempb, (r, a+1), self.RealVal(self.board)))
		else:
			if self.board.b[1] == self.board.b[4]:
				if self.board.b[2] == self.board.b[3]:
					for r in [0, 1, 2, 5]:
						if not self.board.row_empty(r):
							for a in range(self.board.spot_avail(r)):
								tempb = self.board.dupe()
								tempb.update_b(r, a+1)
								self.children.append(Node(self.depth - 1, -1*self.pnum, tempb, (r, a+1), self.RealVal(self.board)))
				else:
					for r in [0, 1, 2, 3, 5]:
						if not self.board.row_empty(r):
							for a in range(self.board.spot_avail(r)):
								tempb = self.board.dupe()
								tempb.update_b(r, a+1)
								self.children.append(Node(self.depth - 1, -1*self.pnum, tempb, (r, a+1), self.RealVal(self.board)))
			else:
				if self.board.b[2] == self.board.b[3]:
					for r in [0, 1, 2, 4, 5]:
						if not self.board.row_empty(r):
							for a in range(self.board.spot_avail(r)):
								tempb = self.board.dupe()
								tempb.update_b(r, a+1)
								self.children.append(Node(self.depth - 1, -1*self.pnum, tempb, (r, a+1), self.RealVal(self.board)))
				else:
					for r in range(6):
						if not self.board.row_empty(r):
							for a in range(self.board.spot_avail(r)):
								tempb = self.board.dupe()
								tempb.update_b(r, a+1)
								self.children.append(Node(self.depth - 1, -1*self.pnum, tempb, (r, a+1), self.RealVal(self.board)))

		# if self.depth >= 0 and self.val == 0:
		# 	for r in range(6):
		# 		if not self.board.row_empty(r):
		# 			for a in range(self.board.spot_avail(r)):
		# 				tempb = self.board.dupe()
		# 				tempb.update_b(r, a+1)
		# 				self.children.append(Node(self.depth - 1, -1*self.pnum, tempb, (r, a+1), self.RealVal(self.board)))

	def RealVal(self, b):
		if b.g_o():
			return maxsize * -1 * self.pnum
		elif b.one_left() or b.win_board():
			return maxsize * self.pnum
		return 0

def MinMax(node, depth, pnum):
	if (depth == 0) or (abs(node.val) == maxsize):
		return node.val

	bestV = maxsize * -pnum

	for child in node.children:
		val = MinMax(child, depth - 1, -1 * pnum)
		if abs(maxsize * pnum - val) < abs(maxsize * pnum - bestV):
			bestV = val

	return bestV

def goodDepth(b):
	l = b.num_row()
	s = 0
	for i in l:
		s += i
	if s > 20:
		return 0
	r = 0
	for i in l:
		if i > 0:
			r += 1
	if r > 4 and s > 15:
		return 3
	if r > 3 and s > 10:
		return 4
	if r > 3:
		return 5
	return 6
