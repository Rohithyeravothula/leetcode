class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        prev = [triangle[0][0]]
        h = len(triangle)
        if h==0:
        	return 0
        for i in range(1, h):
        	l = len(triangle[i])
        	cur = [prev[0]+triangle[i][0]]
        	for j in range(1, l-1):
        		entry = min(prev[j], prev[j-1])+triangle[i][j]
        		cur.append(entry)
        	cur.append(prev[-1]+triangle[i][l-1])
        	# print(prev, cur)
        	prev = cur
        return min(prev)


tt=[[1], [2,3]]
s=Solution()
print(s.minimumTotal(tt))
