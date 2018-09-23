def missingWords(s, t):
	s = s.split()
	t = t.split()
	sl = len(s)
	tl = len(t)
	i = 0
	j = 0
	missing = []
	while i<sl or j<tl:
		if i<sl and j<tl and s[i] == t[j]:
			i+=1
			j+=1
		else:
			missing.append(s[i])
			i+=1
	return missing

s = "I am using hackerrank to improve programming"
t = "am hackerrank to improve"
print(missingWords(s, t))