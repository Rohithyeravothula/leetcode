n = int(input())

corner = ["", "O", "OO", "OOO"]
if n<4:
	print(corner[n])

else:
	s=["o"]*(n+1)
	a=1
	b=1
	c=2
	s[0] = "O"
	s[1] = "O"
	s[2] = "O"
	while c<=n:
		s[c] = "O"
		c = a+b
		b=a
		a=c
	print("".join(s[1:]))