def integer_operations(initial_value):
	my_number = initial_value
	my_sum = my_number
	number = 1
	while number <=5:
		next_num = my_number + number
		my_sum += next_num
		number += 1
	return my_sum
