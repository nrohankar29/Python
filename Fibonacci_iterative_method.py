def fib_iter(n):

	a = 0
	b = 1

	for i in range(n):

		a, b = b, a + b

	return a

n = int(input())

print(fib_iter(n))