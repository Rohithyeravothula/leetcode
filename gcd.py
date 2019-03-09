def gcd(x, y):
	if x>y:
		x,y = y,x
	if x==y or x==0:
		return y
	return gcd(x, y%x)

print(gcd(10,4))