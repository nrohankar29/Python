def parentheses_checker(s):

	stack = []

	for char in s:

		if char == '(' or char == '{' or char == '[':

			stack.append(char)

		if char == ')' or char == '}' or char == ']':

			stack.pop()

	if len(stack) == 0:

		print('balanced')

	else:

		print('not balanced')

t = int(input())

for i in range(t):

	s = input()

	print(parentheses_checker(s))