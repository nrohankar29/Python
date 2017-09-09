def parentheses_checker(s):

	if len(s) % 2 != 0:
	
		return 'not balanced'

	opening = set('([{')

	matches = set([('(',')'), ('[',']'), ('{','}')])

	stack = []

	for paren in s:

		if paren in opening:

			stack.append(paren)

		else:

			if len(stack) is 0:

				return 'not balanced'

			last_open = stack.pop()

			if (last_open,paren) not in matches:

				return 'not balanced'

	if len(stack) == 0:

		return 'balanced'

	else:

		return 'not balanced'

t = int(input())

for num in range(t):

	s = input()

	print (parentheses_checker(s))