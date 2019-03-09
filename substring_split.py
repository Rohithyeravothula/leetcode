def split_str(s, n):
	l = len(s)
	k = l//n
	r = l%n
	prev = 0
	while prev < l:
		carry = 1 if r>0 else 0
		r-=1
		ni = k+carry
		print(prev, ni)
		print(s[prev:prev+ni])
		prev += ni

split_str("abcdefg", 3)
