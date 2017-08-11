def large_count_sum(arr):

	if len(arr) == 0:
		return 0

	max_sum = current_sum = arr[0]

	for num in arr[1:]:

		current_sum = max(current_sum + num, num)

		max_sum = max(current_sum, max_sum)

	return max_sum

t = int(input())

for i in range(t):

	n = int(input())

	arr1 = list(map(int, input().split()))

	print(large_count_sum(arr1))