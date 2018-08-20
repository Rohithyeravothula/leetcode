def missingWords(s, t):
	s = s.split()
	t = t.split()
	ls = len(s)
	lt = len(t)

	response = []
	i = 0
	j = 0
	while i < ls and j < lt:
		if s[i] == t[j]:
			i+=1
			j+=1
		else:
			response.append(s[i])
			i+=1
	while i < ls:
		response.append(s[i])
		i += 1
	return response

s = ""
t = ""
# s = "I like cheese and cake"
# t = "I like cheese and"
# s = ""
# t = "hello this is test"
# s = "I am hackerrank test"
# t = "I hackerrank"
print(missingWords(s, t))
		