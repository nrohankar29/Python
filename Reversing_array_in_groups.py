def reverseInGroups(arr,n,k):
	for i in range(0,n,k):
		start = i
		end = min(i+k-1,n-1)
		while start < end:
			arr[start],arr[end] = arr[end],arr[start]
			start += 1
			end -= 1
	for i in arr:
		print(i,end=" ")
	print()
t = int(input())
for i in range(t):
	n = int(input())
	arr = [x for x in input().split()]
	k = int(input())
	reverseInGroups(arr,n,k)