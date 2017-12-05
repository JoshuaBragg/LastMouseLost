from sys import maxsize

class Node:
	def __init__(self, depth, pnum, board, move = (0, 0), val = 0):
		self.depth = depth
		self.pnum = pnum
		self.board = board
		self.val = val
		self.move = move
		self.children = []
		self.CreateChildren()	
	
	def CreateChildren(self):
		if self.depth >= 0:
			for r in range(6):
				if not self.board.row_empty(r):
					for a in range(self.board.spot_avail(r)):
						tempb = self.board.dupe()
						tempb.update_b(r, a+1)
						self.children.append(Node(self.depth - 1, -1*self.pnum, tempb, (r, a+1), self.RealVal(self.board)))
						
	def RealVal(self, b):
		if b.g_o():
			return maxsize * -1 * self.pnum
		elif b.one_left():
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
