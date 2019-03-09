def customSort(arr):
	frequency = {}
	for val in arr:
		if val in frequency:
			frequency[val] += 1
		else:
			frequency[val] = 1
	numbers = [(val, key) for key, val in list(frequency.items())]
	numbers.sort()
	for freq, num in numbers:
		for _ in range(freq):
			print(num)

customSort([3,8,7,1,1])