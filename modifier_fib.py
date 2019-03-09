def fib(t1, t2, n):
	for i in range(n-2):
		t1, t2 = t2, t1+t2**2
	return t2
print(fib(0,1,9))


