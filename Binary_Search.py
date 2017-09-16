def bin_search(arr,left,right,ele):
    
    arr.sort()

    if right >= left:

        mid = left + ((right - left) // 2)

        if arr[mid] == ele:

            return (mid+1)

        elif arr[mid] > ele:

            return bin_search(arr,left,mid-1,ele)

        else:

            return bin_search(arr,mid+1,right,ele)

    else:

        return -1

N = int(input())
arr = list(map(int,input().split(' ')))
q = int(input())
for i in range(q):
    ele = int(input())
    print(bin_search(arr,0,len(arr)-1,ele))