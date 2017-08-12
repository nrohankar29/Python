def str_compress(s):

	l = len(s)
	r = ""

	if l == 0:
		return ""

	if l == 1:
		return s + "1"

	count = 1

	i = 1

	while i < l:

		if s[i] == s[i-1]:

			count += 1

		else:

			r = r + s[i-1] + str(count)

			count = 1

		i += 1

	r = r + s[i-1] + str(count)

	return r

t = int(input())

for num in range(t):

	s = input()

	print(str_compress(s))