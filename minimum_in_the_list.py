#Write two Python functions to find the minimum number in a 
#list. The first function should compare each number to every 
#other number on the list. O(n2). The second function 
#should be linear O(n).

import time
from random import randrange

def findMin(alist):#O(n2)
	overallMin = alist[0]
	for i in alist:
		issmallest = True
		for j in alist:
			if i > j:
				issmallest = False
		if issmallest:
			overallMin = i
	return overallMin

#alist = list(map(int, input().split()))
#print(findMin(alist))

for listSize in range(1000,10001,1000):
	alist = [randrange(100000) for x in range(listSize)]
	start = time.time()
	print(findMin(alist))
	end = time.time()
	print("size: %d time: %f" % (listSize, end-start))