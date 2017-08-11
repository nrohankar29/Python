#def rev_word1(s):
#	return " ".join(reversed(s.split()))

#Or

#def rev_word2(s):
#	return " ".join(s.split()[::-1])

def rev_word3(s):

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

	return words

#print(rev_word3('   before    something   '))

def reverselist1(words):
    
    start = 0
    
    end = len(words) - 1
    
    while start < end:
        
        words[start], words[end] = words[end], words[start]
        
        start += 1
        
        end -= 1
        
    return ' '.join(words)

print(reverselist1(rev_word3('    before   something   ')))