class Queue:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self,item):
		self.items.insert(0,item)
		print(str(item) + " pushed to the queue")

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

q = Queue()
print(q.size())
print(q.isEmpty())
print(q.enqueue(1))
print(q.dequeue())