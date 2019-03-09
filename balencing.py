def balence(s, m):
	c = 0
	for val in s:
		if val == "<":
			c+=1
		elif val == ">":
			c-=1
			if c<0:
				if m>0:
					m-=1
					c+=1
				elif m<=0:
					break
	return c==0
def balencedOrNot(exp, changes):
	return [1 if balence(e,m) else 0 for e,m in zip(exp, changes)]


s="<>"
s="<><><<<>>><><"
s=""
s=">>"
print(balence(s, 2))
# print(balencedOrNot([s], [0]))
