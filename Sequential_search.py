def seq_search(arr,ele):

	pos = 0

	found = False

	while pos < len(arr) and not found:

		if arr[pos] == ele:

			found = True

		else:

			pos += 1

	return found

arr = list(map(int, input().split()))

print(seq_search(arr,int(input())))