def uniq_char(s):

	for i in range(len(s)):

		j = i + 1

		while j < len(s):

			if s[i] == s[j]:

				return False

			j += 1

	return True

t = int(input())

for num in range(t):

	s = input()

	print(uniq_char(s))