def reverse(s):

	words = []
	length = len(s)
	spaces = [' ']

	i = 0

	while i < length:

		if s[i] not in spaces:

			word_start = i

			while i < length and s[i] not in spaces:

				i += 1

			words.append(s[word_start:i])

		i += 1

	words2 = []

	for i in words:

		words2.insert(0,i)

	return(str.join(' ',words2))

t = int(input())

for i in range(t):

	s = input()

	print(reverse(s))