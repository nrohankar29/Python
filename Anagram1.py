s1 = raw_input()
s2 = raw_input()

def anagram1(s3,s4):
	
	s3 = s3.replace(' ','').lower()
	s4 = s4.replace(' ','').lower()

	return sorted(s3) == sorted(s4)

print anagram1(s1,s2)
