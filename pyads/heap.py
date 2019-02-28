class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.size = 0
	
	def percUp(self, i):
		while i // 2:
			if self.heapList[i] < self.heapList[i // 2]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[i // 2]
				self.healpList[i // 2] = tmp
			i //= 2
			
	
	def insert(self, data):
		self.heapList.append(data)
		self.size += 1
		self.percUp(self.size)
	
	