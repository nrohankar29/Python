def distance(dna1,dna2):
	if len(dna1) != len(dna2):
		raise ValueError("DNA strands are not of same length")

	hamming_dintance = 0

	for i in range(len(dna1)):
		if dna1[i] != dna2[i]:
			hamming_dintance += 1

	return hamming_dintance