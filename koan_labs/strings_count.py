def count_letter_b(string):
	bCount = 0
	for letter in string:
		if letter.lower() == "b":
			bCount += 1
	return bCount
