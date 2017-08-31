def maxSubArraySum(a):

	max_so_far = 0
	max_ending_here = 0

	for i in range(len(a)):
		max_ending_here = max_ending_here + a[i]
		if max_ending_here < 0:
			max_ending_here = 0
		# Do not compare for all elements. Compare only
		# when max_ending_here > 0

		elif (max_so_far < max_ending_here):
			max_so_far = max_ending_here

	return max_so_far

t = int(input())

for i in range(t):
	a = list(map(int,input().split()))
	print(maxSubArraySum(a))