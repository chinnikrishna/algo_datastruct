class BTNode:
	def __init__(self, data):
		self.key = data
		self.left = None
		self.right = None
		self.parent = None

class BinarySearchTree:
	def __init__(self):
		self.root = None
	
	def insNode(self, data):
		# Create a new node
		n = BTNode(data)
		# If tree is empty create the first one
		if self.root == None:
			self.root = n
		else:
			# Get the root
			curr = self.root
			# Iterate until you reach the right leaf node
			while curr is not None:
				# Keep track present parent
				parent = curr
				# Go left if less
				if data < curr.key:
					curr = curr.left
				# Go right if greater
				else:
					curr = curr.right
			# Now insert
			if data < parent.key:
				parent.left = n
			else:
				parent.right = n
			n.parent = parent
	
	
	def preOrder(self, root):
		if root:
			print(root.key)
			self.preOrder(root.left)
			self.preOrder(root.right)
			

	

bst = BinarySearchTree()
bst.insNode(10)
bst.insNode(67)
bst.insNode(42)
bst.insNode(23)
bst.insNode(89)
bst.insNode(34)
bst.preOrder(bst.root)		
	


print("LOL")
	