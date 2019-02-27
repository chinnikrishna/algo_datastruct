from list import DoubleLL

class Queue:
	def __init__(self, maxSize=25):
		self.maxSize = maxSize
		self.qu = DoubleLL()
		self.quSize = 0
	
	def enqueue(self, data):
		if not self.isFull():
			self.qu.prepend(data)
			self.quSize += 1
		else:
			print("Queue is full")
	
	def dequeue(self):
		if not self.isEmpty():
			value = self.qu.tail.value
			self.qu.delLastNode()
			self.quSize -= 1
		else:
			print("Queue is empty")
	
	def isFull(self):
		return (self.quSize == self.maxSize)
	
	def isEmpty(self):
		return (self.quSize == 0)
		
	def printQueue(self):
		self.qu.printList()
	