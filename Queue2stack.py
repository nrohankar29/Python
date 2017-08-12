class Queue2stacks:

	def __init__(self):

		self.instack = []
		self.outstack = []

	def enqueue(self,element):

		self.instack.append(element)

	def dequeue(self):

		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())

		return self.outstack.pop()

q = Queue2stacks()

for i in range(5):
	q.enqueue(i)

for i in range(5):
	print(q.dequeue())