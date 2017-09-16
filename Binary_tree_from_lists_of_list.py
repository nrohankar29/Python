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

def BinaryTree(r):
	return [r, [], []]

def insertLeft(root,newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])
	return root

def insertRight(root,newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2,[newBranch,[],t])
	else:
		root.insert(2,[newBranch,[],[]])
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root,newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

def buildTree():
	r = BinaryTree('a')
	#print(r)
	insertLeft(r,'b')
	#print(r)
	insertRight(r,'c')
	#print(r)
	insertRight(getLeftChild(r),'d')
	#print(r)
	insertLeft(getRightChild(r),'e')
	#print(r)
	insertRight(getRightChild(r),'f')
	return r

ttree = buildTree()
testEqual(getRootVal(getRightChild(ttree)),'c')
testEqual(getRootVal(getRightChild(getLeftChild(ttree))),'d')
testEqual(getRootVal(getRightChild(getRightChild(ttree))),'f')