
def getScore(s):
	if not s:
		return 0
	l = len(s)
	opt = [[0]*l for _ in range(l)]
	for i in range(l):
		opt[i][i] = 1

	for i in range(l-1):
		opt[i][i+1] = 1
		if s[i] == s[i+1]:
			opt[i][i+1] = 2


	k = 2
	while k<l:
		for i in range(l-k):
			j = i+k
			opt[i][j] = max(opt[i][j-1], opt[i+1][j])
			if s[i] == s[j]:
				opt[i][j] = max(opt[i][j], 2+opt[i+1][j-1])
		k+=1
	max_columns = []
	for j in range(0, l):
		max_columns.append(max(opt[j]))

	# for row in opt:
	# 	print(row)

	max_right = [0]*l
	for index, row in enumerate(opt):
		max_right[index] = max(row)

	# for i in range(1, l):
	# 	max_right[i] = max(max_right[i], max_right[i-1])
	for i in range(l-2, -1, -1):
		max_right[i] = max(max_right[i], max_right[i+1])

	
	for i in range(l):
		for j in range(1, l):
			opt[i][j] = max(opt[i][j], opt[i][j-1])

	max_left = [0]*l
	for i in range(l):
		for j in range(0, i+1):
			max_left[i] = max(max_left[i], opt[j][i])

	# for i in range(l-2, -1, -1):
	# 	max_left[i] = max(max_left[i+1], max_left[i])

	# print(max_left)
	# print(max_right)
	val = 1
	for i in range(1, l):
		# print(max_left[i-1], max_right[i])
		val = max(val, max_left[i-1]*max_right[i])
	return val




print(getScore("acdapmpomp"))
# getScore("yyabcbaefem")
# print(getScore("axbawbaseksqke"))
# print(getScore("eaba"))