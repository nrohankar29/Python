# A Sample Python program for beginners with Competitive Programming

# Returns index of x in arr if it is present,
# else returns -1
def search(arr, x):
	n = len(arr)
	for j in range(0,n):
		if (x == arr[j]):
			return j
	return -1

# Input number of test cases
t = int(raw_input())

# One by one run for all input test cases
for i in range(0,t):

	# Input the size of the array
	n = int(raw_input())

	# Input the array
	arr = map(int, raw_input().split())

	# Input the element to be searched
	x = int(raw_input())

	print(search(arr, x))

	# The element can also be searched by index method
	# But you need to handle the exceptions when the element is not found
	# Uncomment the below line to get that working.
	#arr.index(x)