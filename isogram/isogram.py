def is_isogram(word):
	import string
	word = word.lower()
	for letter in string.ascii_lowercase:
		letter_count = word.count( letter )
		if letter_count > 1:
			return False
	return True