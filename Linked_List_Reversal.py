class Node(object):

	def __init__(self,value):

		self.value = value
		self.nextnode = None

def reverse(head):

	current = head
	prev_node = None
	next_node = None

	while current:

		next_node = current.nextnode

		current.nextnode = prev_node

		prev_node = current
		current = next_node

	return prev_node

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print (a.value)
print (a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)

print (reverse(a))

print (d.value)
print (d.nextnode.value)
print (c.nextnode.value)
print (b.nextnode.value)