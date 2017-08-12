def Uniq_char2(s):

	chars = set()

	for letter in s:

		if letter in chars:

			return False

		else:

			chars.add(letter)

	return True

t = int(input())

for num in range(t):

	s = input()

	print(Uniq_char2(s))