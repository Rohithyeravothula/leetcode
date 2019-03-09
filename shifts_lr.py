def getShiftedString(s, leftshift, rightshift):
	l = len(s)
	leftshift = leftshift%l
	rightshift = rightshift%l
	if leftshift > rightshift:
		leftshift -= rightshift
	else:
		rightshift -= leftshift
		leftshift = l - rightshift
	return s[leftshift:] + s[:leftshift]  

print(getShiftedString("abcd", 2, 3))


