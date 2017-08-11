def rev_string(s):

	s = s.split()

	s = s[::-1]

	s = ' '.join(s)

	return s

s = input()

print(rev_string(s))