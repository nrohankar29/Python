def fib_rec(n):

	# Base Case
	if n ==  0 or n == 1:
		return n

	else:

		return fib_rec(n-1) + fib_rec(n-2)

n = int(input())

print(fib_rec(n))