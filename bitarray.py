def bitarray(n):
	return 1 << n

def setbit(n, i):
	return n | i << (i-1)

def unset(n, i):
	return n & (1 << i)

