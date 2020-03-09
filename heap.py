class Heap:

	def __init__(self):
		self.HeapArray = []
		self.Length = 0
		
	def MakeHeap(self, a, depth):
		self.Length = 2**(depth+1)-1
		for i in range (len(a)):
			if i < self.Length:
				self.HeapArray.append(a[i])
				while i > 0: 
					if i % 2 != 0:
						if self.HeapArray[i] > self.HeapArray[i//2]:
							self.HeapArray[i], self.HeapArray[i//2] = (
								self.HeapArray[i//2], self.HeapArray[i])
							i = i//2
						else:
							i = 0
					else:
						if self.HeapArray[i] > self.HeapArray[i//2-1]:
							self.HeapArray[i], self.HeapArray[i//2-1] = (
								self.HeapArray[i//2-1], self.HeapArray[i])
							i = i//2-1
						else:
							i = 0
			else:
				return

	def GetMax(self):
		if len(self.HeapArray) > 0:
			self.HeapArray[0], self.HeapArray[len(self.HeapArray)-1] = (
				self.HeapArray[len(self.HeapArray)-1], self.HeapArray[0])
			result = self.HeapArray.pop(len(self.HeapArray)-1)
			if len(self.HeapArray) <= 1:
				return result
			else:
				test_node = self.HeapArray[0]
				test_index = 0
				while test_node:
					if 2*test_index+2 <= len(self.HeapArray)-1: 
						if (self.HeapArray[2*test_index+1] > 
							self.HeapArray[2*test_index+2]):
							if (self.HeapArray[2*test_index+1] > 
								self.HeapArray[test_index]):
								(self.HeapArray[2*test_index+1], 
									self.HeapArray[test_index]) = (
									self.HeapArray[test_index], 
									self.HeapArray[2*test_index+1])
								test_index = 2*test_index+1
								test_node = self.HeapArray[test_index]
							else: 
								return result
						else: # если 
							if (self.HeapArray[2*test_index+2] > 
								self.HeapArray[test_index]):
								(self.HeapArray[2*test_index+2],
									self.HeapArray[test_index]) = (
									self.HeapArray[test_index], 
									self.HeapArray[2*test_index+2])
								test_index = 2*test_index+2
								test_node = self.HeapArray[test_index]
							else: 
								return result
					elif 2*test_index+1 <= len(self.HeapArray)-1:
						if (self.HeapArray[2*test_index+1] > 
								self.HeapArray[test_index]):
							(self.HeapArray[2*test_index+1],
								self.HeapArray[test_index]) = (
								self.HeapArray[test_index], 
								self.HeapArray[2*test_index+1])
							test_index = 2*test_index+1
						else: 
							return result
					else:
						return result
		else:
			return -1

	def Add(self, key):
		if len(self.HeapArray) < self.Length:
			self.HeapArray.append(key)
			i = len(self.HeapArray)-1
			while i > 0: 
					if i % 2 != 0:
						if self.HeapArray[i] > self.HeapArray[i//2]:
							self.HeapArray[i], self.HeapArray[i//2] = (
								self.HeapArray[i//2], self.HeapArray[i])
							i = i//2
						else:
							i = 0
					else:
						if self.HeapArray[i] > self.HeapArray[i//2-1]:
							self.HeapArray[i], self.HeapArray[i//2-1] = (
								self.HeapArray[i//2-1], self.HeapArray[i])
							i = i//2-1
						else:
							i = 0
			return True
		else:
			return False
