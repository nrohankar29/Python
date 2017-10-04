import time
from random import randrange

def findMin(alist):
	minsofar = alist[0]
	for i in alist:
		if i < minsofar:
			minsofar = i
	return minsofar

print(findMin([5,4,2,1,0]))
print(findMin([0,4,2,1,5]))

for listSize in range(1000,10001,1000):
	alist = [randrange(100000) for x in range(listSize)]
	start = time.time()
	print(findMin(alist))
	end = time.time()
	print("size: %d time: %f" % (listSize, end-start))