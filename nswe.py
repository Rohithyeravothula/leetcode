def build(s):
	if s[-1] == 'N':
		return [s+s[-1], s+'W', s+'S']
	elif s[-1] == 'S':
		return [s+'W', s+'S', s+'E']
	elif s[-1] == 'W':
		return [s+'N', s+'W', s+'S']
	elif s[-1] == 'E':
		return [s+'N', s+'S', s+'E']

def generate(n):
	if n == 0:
		return []
	cur = ['N', 'S', 'E', 'W']
	for _ in range(n-1):
		newcur = []
		for s in cur:
			newcur.extend(build(s))
		cur = newcur
	print(cur)

generate(3)
