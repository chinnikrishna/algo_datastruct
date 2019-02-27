class BTNode:
	def __init__(self, data):
		self.key = data
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self, rootVal):
		self.root = None
	
	def insNode(self, data):
		n = BTNode(data):
		if self.root == None:
			if(data < self.root):
				self.root.left = n
			else:
				self.root.right = n
		else:
			self.root = n
		
	


print("LOL")
	