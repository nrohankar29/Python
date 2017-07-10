def is_pangram(word):
	check = set()
	for char in word.lower():
		if char.isalpha():
			check.add(char)
	if len(check) == 26:
		return True
	return False
