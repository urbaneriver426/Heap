import unittest

class Heap:

	def __init__(self):
		self.HeapArray = []
		self.Length = 0
		
	def MakeHeap(self, a, depth):
		self.Length = 2**depth-1
		for i in range (len(a)):
			if i < self.Length:
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
				return

	def GetMax(self):
		if len(self.HeapArray) > 0:
			return self.HeapArray[0]
		else:
			return -1

	def Add(self, key):
		if len(self.HeapArray) < self.Length:
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


class TestHeap(unittest.TestCase):
	def setUp(self):
		self.heap = Heap()

	def testMakeEmptyHeap(self):
		x = [1]
		self.heap.MakeHeap(x,0)
		assert len(self.heap.HeapArray) == 0

	def testMakeHalfFullHeap(self):
		x = [1,2,3,4]
		self.heap.MakeHeap(x,3)
		assert self.heap.Length == 7
		assert len(self.heap.HeapArray) == 4

	def testMakeFullHeap(self):
		x = [1,2,3,4,5,6,7]
		self.heap.MakeHeap(x,3)
		assert self.heap.Length == 7
		assert len(self.heap.HeapArray) == 7

	def testMakeFullHeapPlus(self):
		x = [1,2,3,4,5,6,7,8,9]
		self.heap.MakeHeap(x,3)
		assert self.heap.Length == 7
		assert len(self.heap.HeapArray) == 7
		assert 9 not in self.heap.HeapArray
		assert 8 not in self.heap.HeapArray

	def testAddBiggest(self):
		x = [1,2,3,4]
		self.heap.MakeHeap(x,3)
		y = self.heap.Add(20)
		assert len(self.heap.HeapArray) == 5
		assert self.heap.HeapArray[0] == 20
		assert y is True

	def testAddLowest(self):
		x = [2,3,4,5]
		self.heap.MakeHeap(x,3)
		y = self.heap.Add(1)
		assert len(self.heap.HeapArray) == 5
		assert self.heap.HeapArray[4] == 1
		assert y is True

	def testAddSomewhere(self):
		x = [2,6,4,15]
		self.heap.MakeHeap(x,3)
		y = self.heap.Add(5)
		assert len(self.heap.HeapArray) == 5
		assert 5 in self.heap.HeapArray
		assert y is True

	def testAddInEmpty(self):
		x = []
		self.heap.MakeHeap(x,3)
		y = self.heap.Add(10)
		assert self.heap.Length == 7
		assert len(self.heap.HeapArray) == 1
		assert 10 in self.heap.HeapArray
		assert y is True

	def testAddInFull(self):
		x = [1,2,3,4,5,6,7]
		self.heap.MakeHeap(x,3)
		y = self.heap.Add(8)
		assert y is False
		assert 8 not in self.heap.HeapArray

	def testGetMaxEmpty(self):
		x = []
		self.heap.MakeHeap(x,0)
		y = self.heap.GetMax()
		assert y == -1

	def testGetMax(self):
		x = [1,2,3,4]
		self.heap.MakeHeap(x,3)
		y = self.heap.GetMax()
		assert y == 4

if __name__ == '__main__':
	unittest.main()
