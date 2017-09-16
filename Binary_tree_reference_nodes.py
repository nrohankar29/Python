class BinaryTree:
	def __init__(self,rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self,newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self,newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self,obj):
		self.key = obj

	def getRootVal(self):
		return self.key

def buildTree():
	r = BinaryTree('a')
	r.insertLeft('b')
	r.insertRight('c')
	b = r.getLeftChild()
	b.insertRight('d')
	c = r.getRightChild()
	c.insertLeft('e')
	c.insertRight('f')
	return r

def testEqual(actual, expected):
    if type(expected) == type(1):
        # they're integers, so check if exactly the same
        if actual == expected:
            print('Pass')
            return True
    elif type(expected) == type(1.11):
        # a float is expected, so just check if it's very close, to allow for
        # rounding errors
        if abs(actual-expected) < 0.00001:
            print('Pass')
            return True
    else:
        # check if they are equal
        if actual == expected:
            print('Pass')
            return True
    print('Test Failed: expected ' + str(expected) + ' but got ' + str(actual))
    return False

ttree = buildTree()

testEqual(ttree.getRightChild().getRootVal(),'c')
testEqual(ttree.getLeftChild().getRightChild().getRootVal(),'d')
testEqual(ttree.getRightChild().getLeftChild().getRootVal(),'e')
