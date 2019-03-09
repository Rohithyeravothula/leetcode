from collections import defaultdict
class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        pointsset = {(x,y) for (x,y) in points}
        mina = float("inf")
        seen = set()
        for (x1, y1) in points:
        	for (x2, y2) in points:
        		if (x2, y2) in seen:
        			continue
        		(x3,y3) = (x1, y2)
        		(x4,y4) = (x2, y1)
        		if (x3, y3) not in pointsset or (x4, y4) not in pointsset:
        			continue
        		s = {(x1, y1), (x2, y2), (x3, y3), (x4, y4)}
        		if len(s) == 4:
        			mina = min(mina, abs(x2-x1)*abs(y2-y1))
        	seen.add((x1, y1))
        return mina if mina != float("inf") else 0

inp = []
inp = [[3,3],[2,2]]
inp = [[0,0],[0,1],[1,0],[1,1],[1,3],[3,1],[3,3],[2,2]]
inp = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
inp = [[1,1],[1,3],[3,1],[3,3],[2,2]]
print(Solution().minAreaRect(inp))


