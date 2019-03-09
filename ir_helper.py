from math import log2

def dcg(a):
	c = 0
	for i in range(1, 6):
		c += a[i-1]/log2(i+1)
	return c 

while True:
	a = []
	for _ in range(5):
		a.append(float(input()))
	print(dcg(a))
