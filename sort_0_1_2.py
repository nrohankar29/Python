def sort_array(a):
    
    lo = 0

    hi = len(a) - 1

    mid = 0
    
    while mid <= hi:

        if a[mid] == 0:

            a[lo],a[mid] = a[mid],a[lo]

            lo += 1

            mid += 1

        elif a[mid] == 1:

            mid += 1

        else:

            a[mid],a[hi] = a[hi],a[mid]

            hi -= 1

    return a
    
t = int(input())

for i in range(t):
    
    n = int(input())
    
    a = list(map(int, input().split()))
    
    print(sort_array(a))