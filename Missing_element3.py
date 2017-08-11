def finder3(arr1,arr2):

	result = 0

	for num in arr1 + arr2:
		result^=num
		#print result

	return result

arr1 = [5,5,7,7]
arr2 = [5,7,7]

print finder3(arr1,arr2)