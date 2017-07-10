def word_count(phrase):
	phrase2 = list(set(phrase.split()))
	for word in phrase2:
		print word + ":",phrase.count(word)

word_count('one fish two fish red fish blue fish')