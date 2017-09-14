def rec_bin_search(arr,ele):

	if len(arr) == 0:

		return False

	else:

		mid = len(arr)//2

		if arr[mid] == ele:

			return True

		else:

			if ele < arr[mid]:

				return rec_bin_search(arr[:mid],ele)

			else:

				return rec_bin_search(arr[mid+1:],ele)

arr = list(map(int,input().split()))

print(rec_bin_search(arr,int(input())))
