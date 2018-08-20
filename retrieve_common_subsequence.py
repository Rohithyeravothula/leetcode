def missingWords(s, t):
	s = s.split()
	t = t.split()
	ls = len(s)
	lt = len(t)

	if not t:
		return s
	if not s:
		return []
	opt = [[0]*(1+lt) for _ in range(1+ls)]
	for i in range(ls+1):
		for j in range(lt+1):
			if i == 0 or j == 0:
				opt[i][j] = 0
			if s[i-1] == t[j-1]:
				opt[i][j] = 1+opt[i-1][j-1]
			else:
				opt[i][j] = max(opt[i-1][j], opt[i][j-1])

	indices = retrieve_common_sequence(opt, ls, lt, s, t)
	# print(indices)

	# for row in opt:
	# 	print(row)
	response = []
	for index, word in enumerate(s):
		if index not in indices:
			response.append(word)
	return response




def retrieve_common_sequence(opt, l, b, s, t):
	cur_i = l
	cur_j = b
	indices = []
	while cur_i > 0 and cur_j > 0:
		if s[cur_i-1] == t[cur_j-1]:
			if cur_i > 0:
				indices.append(cur_i-1)
			cur_i -= 1
			cur_j -= 1
		else:
			if opt[cur_i - 1][cur_j]  > opt[cur_i][cur_j-1]:
				cur_i -= 1
			else:
				cur_j -= 1
	return set(indices)



# s = "I like cheese and cake"
# t = "I like cheese and"
# s = ""
# t = "hello this is test"
s = "I am hackerrank test"
t = "I hackerrank"
print(missingWords(s, t))



"""
if opt[cur_i-1][cur_j] == opt[cur_i][cur_j-1]:
				if cur_i > 0:
					cur_i -= 1
				else:
					cur_j -= 1
			el
			"""