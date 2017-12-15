import math


def prime_sum(n):
	if n<4:
		return 1
	m = int(math.sqrt(n)) + 1 
	pm = int(math.sqrt(n))
	c=1
	for i in range(2, m):
		if n%i == 0:
			c+=2
		if i == pm:
			c-=1
	return c

def longestSequence(a):
	return sum([primt_sum(i) for i in a])


