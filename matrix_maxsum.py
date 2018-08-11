


def max_sum(a):
	l = len(a)

	if l == 0:
		return 0

	b = len(a[0])

	if l==1 and b==1:
		return a[0][0]

	col_sums = []
	flip_sums = []
	is_zero = False
	for j in range(0, b):
		s = 0
		fs = 0
		for i in range(0, l):
			s+=a[i][j]
			fs += (-1*a[i][j])
		col_sums.append(s)
		flip_sums.append(fs)
		if s==0:
			is_zero = True


	if is_zero:
		total = 0
		for s, fs in zip(col_sums, flip_sums):
			total += max(s, fs)
		return total

	else:
		flips = 0
		for s, fs in zip(col_sums, flip_sums):
			if s<fs:
				flips += 1

		balence = 0
		if flips%2!=0:
			min_pos_ary = [s for s in col_sums if s>0]
			if min_pos_ary:
				min_pos = min(min_pos_ary)
			else:
				min_pos = float("inf")
			min_neg = max([s for s in col_sums if s<0])
			if -1*min_neg > min_pos:
				balence = -2*min_pos
			else:
				balence = 2*min_neg
		total = 0
		for s, fs in zip(col_sums, flip_sums):
			total += max(s, fs)
		return total + balence


# mtrix = [[-1, 1, -1], [-1,1,1], [1,1,-1]]
# mtrix = [[0, -3, 3], [0, -2, 2], [0, -1, 1]]
# mtrix = [[-10, -10, -10], [-10, -10, -10]]
print(mtrix)
print(max_sum(mtrix))


