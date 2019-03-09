from heapq import heapify, heappop, heappush
def maximumAmount(a, k):
	a.sort(reverse=True)
	i = 1
	l = len(a)
	profit = 0
	while i<l and k:
		if a[i] != a[i-1]:
			d = (a[i-1] - a[i])*i
			print(d, a[i], a[i-1])
			if d < k:
				s = a[i-1] - a[i]
				profit += (a[i]+1)*s + ((s*(s-1))//2)*i
				k -= d
			else:
				return profit + a[i]*k
		i+=1
	print(profit, k)
	if k>0:
		profit += a[0]*(k//a[0])
	return profit

# print(maximumAmount([5,2,8,4,10,6], 20))
# print(maximumAmount([3,3], 6))
print(maximumAmount([2,2,5], 4))

# x,y = ((n*(n+1))//2), ((p*(p+1))//2)
# print(x,y,x-y)
