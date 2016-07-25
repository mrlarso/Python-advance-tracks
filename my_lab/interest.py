def compounded_principal(time):
	principal = 10000
	amount = principal * ((1.08)**time)
	return amount

print compounded_principal(10)
