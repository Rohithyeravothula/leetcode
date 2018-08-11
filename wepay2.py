from heapq import heappush, heappop
import math
def power_number(n):
	seen = set()
	pool = []
	heappush(pool, (4, (2,2)))
	count = 0
	while True:
		print(pool)
		count += 1
		(val, (x, y)) = heappop(pool)
		if count == n:
			return val
		if (x+1, y) not in seen:
			seen.add((x+1, y))
			heappush(pool, (int(math.pow(x+1, y)), (x+1, y)))
		if (x, y+1) not in seen:
			seen.add((x, y+1))
			heappush(pool, (val*x, (x, y+1)))

print(power_number(10))