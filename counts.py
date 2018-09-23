import operator as op
from functools import reduce

def ncr(n, r):
	r = min(r, n-r)
	numerator = reduce(op.mul, range(n, n-r, -1), 1)
	denominator = reduce(op.mul, range(1, r+1), 1)
	return numerator//denominator


def countTeams(skills, k, l, r):
    n = sum([1 if s>=l and s<=r else 0 for s in skills])
    ans = 0
    for r in range(k, n+1):
    	ans += ncr(n, r)
    return ans



# sks = [12, 4, 6, 13, 5, 10]
# k = 3
# l = 4
# r = 10
# sks = [4,8,5,6]
# k = 1
# l = 5
# r = 7
# print(countTeams(sks, k, l, r))
