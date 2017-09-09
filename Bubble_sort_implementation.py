def bubble_sort(arr):

	numOfSwaps = 0

	for n in range(len(arr)-1,0,-1):

		currentSwaps = 0

		for k in range(n):

			if arr[k] > arr[k+1]:

				temp = arr[k]

				arr[k] = arr[k+1]

				arr[k+1] = temp

				currentSwaps += 1

				numOfSwaps += 1

		if currentSwaps == 0:

			break

	print('Array is sorted in',numOfSwaps,'swaps.')
	print('First Element:',arr[0])
	print('Last Element:',arr[len(arr)-1])
	return

arr = [3,2,1]

print(bubble_sort(arr))