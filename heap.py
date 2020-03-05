class Heap:

	def __init__(self):
		self.HeapArray = []
		
	def MakeHeap(self, a, depth):
		self.lenth = 2**depth-1
		for i in range (len(a)):
			if i < self.lenth:

				self.HeapArray.append(a[i])
				while i > 0: 
					if i % 2 != 0:
						if self.HeapArray[i] > self.HeapArray[i//2]:
							self.HeapArray[i], self.HeapArray[i//2] = (self.HeapArray[i//2], 
							self.HeapArray[i])
							i = i//2
						else:
							i = 0
					else:
						if self.HeapArray[i] > self.HeapArray[i//2-1]:
							self.HeapArray[i], self.HeapArray[i//2-1] = (self.HeapArray[i//2-1], 
							self.HeapArray[i])
							i = i//2-1
						else:
							i = 0
			else:
				print(i)
				return

	def GetMax(self):
		if len(self.HeapArray) > 0:
			return self.HeapArray[0]
		else:
			return -1

	def Add(self, key):
		if len(self.HeapArray) < self.lenth:
			self.HeapArray.append(key)
			i = len(self.HeapArray)-1
			while i > 0: 
					if i % 2 != 0:
						if self.HeapArray[i] > self.HeapArray[i//2]:
							self.HeapArray[i], self.HeapArray[i//2] = (self.HeapArray[i//2], 
							self.HeapArray[i])
							i = i//2
						else:
							i = 0
					else:
						if self.HeapArray[i] > self.HeapArray[i//2-1]:
							self.HeapArray[i], self.HeapArray[i//2-1] = (self.HeapArray[i//2-1], 
							self.HeapArray[i])
							i = i//2-1
						else:
							i = 0
			return True
		else:
			return False
