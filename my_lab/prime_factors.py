def is_prime(number):
	divisor = 2
	factors = []
	while divisor < number:
		if number%divisor == 0:
			factors.append(divisor)
		divisor += 1
	print factors
	if len(factors) == 0:
		return True
	else:
		return False

def largest_prime_factor(args):
	biggest_prime = 1
	divisor = 1
	while divisor < args:
		if args%divisor == 0 and is_prime(divisor):
			biggest_prime = divisor
		divisor += 1

	print biggest_prime
	return biggest_prime

largest_prime_factor(13195)

print is_prime(7)
