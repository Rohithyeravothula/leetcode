def longest(s):
	s = s.split()
	w = [len(w) for w in s]
	we = max([l if l&1==0 else 0 for l in w])
	for w in s:
		if len(w) == we:
			return w

print(longest("hello world this is new"))