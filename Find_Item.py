def findNode(self, node, val):
	if (node is None):
		return False
	elif (node == node.val):
		return True
	elif (node < node.val):
		return self.findNode(nodeLeftChild, val)
	else:
		return self.findNode(nodeRightChild, val)

