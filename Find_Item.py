class Node:
	def __init__(self,val):
		self.value = val
		self.leftChild = None
		self.rightChild = None

	def insert(self, data):
		if self.value == data:
			return False
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				self.leftChild = Node(data)
				return True
		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
				return True
	def find(self, data):
		if(self.value == data):
			return True
		elif (self.value > data):
			if self.leftChild:
				return self.leftChild.find(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.find(data)
			else:
				return False


class Tree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True
	def find(self,data):
		if self.root:
			return self.root.find(data)
		else:
			return False




def findNode(self, node, val):
	if (node is None):
		return False
	elif (node == node.val):
		return True
	elif (node < node.val):
		return self.findNode(nodeLeftChild, val)
	else:
		return self.findNode(nodeRightChild, val)

def 