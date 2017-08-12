class Queue2Satck2:

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

	def peek(self):
		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())
		return self.outstack[len(self.outstack) - 1]

q = Queue2Satck2()
t = int(input())
for num in range(t):

	values = list(map(int, input().split()))
	if values[0] == 1:
		q.enqueue(values[1])
	elif values[0] == 2:
		q.dequeue()
	else:
		print(q.peek())