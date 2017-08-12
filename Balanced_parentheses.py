def balance_check(s):

	count = 0

	for i in s:

		if i == '(' or i == '[' or i == '{':

			count += 1

		elif i == ')' or i == ']' or i == '}':

			count -= 1

	return count == 0

t = int(input())

for num in range(t):

	s = input()

	print(balance_check(s))