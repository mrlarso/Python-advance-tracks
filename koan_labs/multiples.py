def multiple_sum():
	the_sum = 0
	number = 1
	while number < 1000:
		if number%3 == 0 or number%5 == 0:
			the_sum += number
		number += 1
	return the_sum
