def countMoves(numbers):
	m = min(numbers)
	return sum(list(map(lambda x: x-m, numbers)))
a=[1,2,3]
print(countMoves(a))