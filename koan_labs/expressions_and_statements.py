def compounded_principal(time):
	principal = 10000
	amount = principal * (1.08)**time
	return int(round(amount))
