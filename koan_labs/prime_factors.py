def is_prime(number):
	for divisor in range(2,number):
		if number%divisor == 0:
			return False
	return True


def largest_prime_factor(args):
	biggest_prime = 1
	for divisor in range (2,args):
		if args%divisor == 0 and is_prime(divisor):
			biggest_prime = divisor
	return biggest_prime
