# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, a: 'List[Interval]', b: 'List[Interval]') -> 'List[Interval]':
    	l = len(a)
    	m = len(b)
    	i,j = 0,0
    	ans = []
    	while i<l and j<m:
    		if a[i].end < b[j].start:
    			i+=1
    		elif b[j].end < a[i].start:
    			j+=1
    		else:
    			ans.append([max(a[i].start, b[j].start), min(a[i].end, b[j].end)])
    			if a[i].end < b[j].end:
    				i+=1
    			else:
    				j+=1
    	return ans

a = [[0,2],[5,10],[13,23],[24,25], [28,28]]
b = [[1,5],[8,12],[15,24],[25,26], [28,28]]
a,b=[[1,4],[5,9],[10,13]],[[8,10]]
print(Solution().intervalIntersection(a, b))