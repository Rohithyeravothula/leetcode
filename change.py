changes = {'PENNY': 0.01,'NICKEL': 0.05,'DIME': 0.10,'QUARTER': 0.25,'HALF DOLLAR': 0.50,'ONE': 1.0,'TWO': 2.0,'FIVE': 5.0,'TEN': 10.0,'TWENTY': 20.0,'FIFTY': 50.0,'ONE HUNDRED': 100.0}
denomination = ['PENNY', 'NICKEL', 'DIME', 'QUARTER', 'HALF DOLLAR', 'ONE', 'TWO', 'FIVE', 'TEN', 'TWENTY', 'FIFTY', 'ONE HUNDRED']
denomination = denomination[::-1]

def check():
	pp, ch = map(float, input().split(";"))

	if ch < pp:
		return "ERROR"
	elif ch == pp:
		return "Zero"

	ch = ch - pp

	response = []
	i = 0
	while ch >= 0 and i < len(denomination):
		# print(denomination[i], ch)
		if changes[denomination[i]] <= ch:
			ch -= changes[denomination[i]]
			response.append(denomination[i])
		else:
			i += 1

	response.sort()
	print(" ".join(response))

check()