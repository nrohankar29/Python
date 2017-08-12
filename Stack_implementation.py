class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)
		print(item + " pushed to stack ")

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

s = Stack()

s.push(str(10))
s.push(str(20))
s.push(str(30))

print(s.pop() + " popped from stack")
print("Top item is " + s.peek())