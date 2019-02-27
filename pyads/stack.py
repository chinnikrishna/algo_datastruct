from list import SingleLL

class Stack:
	def __init__(self, maxSize=25):
		self.maxSize=maxSize
		self.stk = SingleLL()
		self.stkSize = 0
	
	def push(self, data):
		if not self.isFull():
			self.stk.append(data)
			self.stkSize += 1
		else:
			print("Stack is Full")
	
	def pop(self):
		if not self.isEmpty():
			value = self.stk.head.value
			self.stk.delFirstNode()
			self.stkSize -= 1
			return value
		else:
			print("Stack is Empty")
	
	def printStack(self):
		self.stk.printList()

	def isFull(self):
		return (self.stkSize == self.maxSize)
	
	def isEmpty(self):
		return (self.stkSize == 0)