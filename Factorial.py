def factorial(n):

	if n == 0:
		return 1

	else:
		return n * factorial(n-1)

t = int(input())
print('\n')

for num in range(t):

	n = int(input())

	print(factorial(n))

	print('\n')