import math
def estimate_fib(n):
	a=1
	b=1
	for i in range(3, n):
		c=a+b
		if i%1000==0:
			print(str(c)[:10],1+int(math.log(c,2)), i)
		b=a
		a=c

estimate_fib(10003)