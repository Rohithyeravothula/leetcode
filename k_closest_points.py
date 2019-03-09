from heapq import heappush, heappop, heappushpop
from math import sqrt
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def get_odist(x,y):
        	return sqrt(x*x + y*y)
        h = []
        i = 0
        l = len(points)
        while i<l and i<k:
        	x,y = points[i]
        	heappush(h, (-get_odist(x,y), [x,y]))
        	i+=1

        while i<l:
        	x,y = points[i]
        	d = -get_odist(x,y)
        	if d > h[0][0]:
        		heappushpop(h, (d, [x,y]))
        	i+=1
        ans = []
        while h:
        	ans.append(heappop(h)[1])
        return ans[::-1]

inp = [[1,3],[-2,2]]
inp = [[3,3],[5,-1],[-2,4]]
print(Solution().kClosest(inp, 2))

