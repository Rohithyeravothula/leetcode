def get_key(info, i, j):
	return info[i][j]


def build_key(nums):
	l = len(nums)
	opt = [[""]*l for _ in range(l)]
	opt[0][0] = str(nums[0])
	for i in range(1, l):
		opt[0][i] = opt[0][i-1] + "-" + str(nums[i])

	for i in range(1, l):
		opt[i][i] = str(nums[i])
		for j in range(i+1, l):
			opt[i][j] = opt[i][j-1] + "-" + str(nums[j])

	return opt




def evenSubarray(numbers, k):
	if not numbers:
		return 0
	l = len(numbers)
	odds = [0]*l
	if numbers[0] & 1:
		odds[0] = 1

	for i in range(1, l):
		odds[i] = odds[i-1] + (numbers[i]&1)

	info = build_key(numbers)

	ans = 0
	seen = set()
	for i in range(l):
		if odds[i] <= k:
			ans += 1
			seen.add(get_key(info, 0, i))
			# seen.add("-".join(map(str, numbers[:i+1])))
		for j in range(i):
			if odds[i] - odds[j] <= k:
				cur_id = get_key(info, j+1, i)
				# cur_id = "-".join(map(str, numbers[j+1:i+1]))
				# print(seen, cur_id)
				if cur_id not in seen:
					ans += 1
					seen.add(cur_id)
	print(seen)
	return ans

nbs = [1,2,3,4]
k = 1
# nbs = []
# k = 1
# nbs = [2,1,2,1,3]
# k = 2
nbs = [2,1,2,1]
k = 2
print(evenSubarray(nbs, k))
# build_key(nbs)


