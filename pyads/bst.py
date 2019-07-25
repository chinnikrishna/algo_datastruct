class BTNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None


class BST:

	def __init__(self):
		self.root = None
		self.size = 0

	def addNode(self, data):
		# Add a new BT Node
		n = BTNode(data)
		# Now figure out where to add this
		# If the root is none, make it the first node
		if self.root is None:
			self.root = n
		else:
			# Get current root
			curr = self.root
			# Keep going until you find leaf node
			while curr is not None:
				parent = curr
				if n.data < curr.data:
					curr = curr.left
				else:
					curr = curr.right
			# Insert data
			if n.data < parent.data:
				parent.left = n
			else:
				parent.right = n
			n.parent = parent
	
	def inOrder(self, root):
		if root is not None:
			self.inOrder(root.left)
			print(root.data)
			self.inOrder(root.right)
	
	def preOrder(self, root):
		if root is not None:
			print(root.data)
			self.preOrder(root.left)
			self.preOrder(root.right)
	
	def postOrder(self, root):
		if root is not None:
			self.postOrder(root.left)
			self.postOrder(root.right)
			print(root.data)


			

bst = BST()
t = [7,8,2,9,4,1]

for i in t:
	bst.addNode(i)

bst.preOrder(bst.root)
print("================")
bst.inOrder(bst.root)
