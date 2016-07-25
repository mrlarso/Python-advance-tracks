def count_letter_b(string):
	b_count = 0
	for i in range(0,len(string)):
		if string[i].lower() == "b":
			b_count += 1
	return b_count
