def ordered_Sequential_Search(arr,ele):

	pos = 0
	found = False
	stop = False

	while pos < len(arr) and not found and not stop:
		if arr[pos] == ele:
			found = True
		else:
			if arr[pos] > ele:
				stop = True
			else:
				pos = pos + 1

	return found

arr = list(map(int,input().strip().split(' ')))
print(ordered_Sequential_Search(arr,int(input().strip())))