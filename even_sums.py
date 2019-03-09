class Solution:
    def sumEvenAfterQueries(self, a: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
    	s = sum([i for i in a if not i&1])
    	ans = []
    	for val, index in queries:
    		if (val%2==0 and a[index]%2==0):
    			s += val
    		elif (val%2==1 and a[index]%2==1):
    			s += (val + a[index])
    		elif (a[index]%2==0 and val%2==1):
    			s -= a[index]
    		a[index] += val
    		ans.append(s)
    	return ans

s = Solution()
a,q = [1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]
a,q = [1,2,3,4], [[3,2], [-1, 2]]
a,q = [], []
print(s.sumEvenAfterQueries(a, q))
        