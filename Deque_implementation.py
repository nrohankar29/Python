class Deque:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self,item):
		self.items.insert(0,item)

	def addRear(self,item):
		self.items.append(item)

	def removeFront(self):
		return self.items.pop(0)

	def removeRear(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

d = Deque()
d.addRear('hello')
d.addFront('world')
print(d.size())
print(d.removeRear() + ' ' + d.removeFront())
print(d.size())