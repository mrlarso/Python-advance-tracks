def is_prime(number):
	divisor = 2
	factors = []
	while divisor < number:
		if number%divisor == 0:
			factors.append(divisor)
			break
		if divisor%2 == 0:
			divisor += 1
		else:
			divisor += 2

	if len(factors) == 0:
		return True
	else:
		return False

def largest_prime_factor(args):
	biggest_prime = 1
	divisor = 2
	while divisor < args:
		if args%divisor == 0 and is_prime(divisor):
			biggest_prime = divisor
		if divisor%2 == 0:
			divisor += 1
		else:
			divisor += 2

	return biggest_prime
