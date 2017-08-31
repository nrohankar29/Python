def missing_number(a):

	n = len(a) + 1

	sum1 = n * (n + 1) / 2

	sum2 = 0

	for i in range(len(a)):

		sum2 += a[i]

	return (int(sum1 - sum2))

t = int(input())

for i in range(t):

	n = int(input())

	a = list(map(int, input().split()))

	print(missing_number(a))


# getMissingNo takes list as argument
#def getMissingNo(A):
#    n = len(A)
#    total = (n+1)*(n+2)/2
#    sum_of_A = sum(A)
#    return total - sum_of_A
 
# Driver program to test above function
#A = [1, 2, 4, 5, 6]
#miss = getMissingNo(A)
#print(miss)
# This code is contributed by Pratik Chhajer
