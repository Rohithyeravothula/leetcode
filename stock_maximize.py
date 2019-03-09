from heapq import heappush, heappop, heapify
def stockmax(prices):
	a = [(-1*val, idx) for idx, val in enumerate(prices)]
	heapify(a)
	profit = 0
	seen = set()
	while a:
		cur, idx = heappop(a)
		cur = -cur
		i = idx-1
		seen.add(idx)
		while i>=0 and i not in seen:
			profit -= prices[i]
			seen.add(i)
			i-=1
		profit += (idx-i-1)*prices[idx]
	return profit



inp = [1,100,1]
inp = [1,100]
inp = [1,2,4,2,8,10]
inp = [1,2,10,4,5,8]
print(stockmax(inp))
