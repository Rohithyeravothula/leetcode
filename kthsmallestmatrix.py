import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def get_next(x, y, l, b):
        	ans = []
        	if x+1<l:
        		ans.append((x+1, y))
        	if y+1<b:
        		ans.append((x, y+1))
        	return ans

        l = len(matrix)
        b = len(matrix[0])
        mins = []
        heapq.heappush(mins, (matrix[0][0], (0,0)))
        count = 0
        visited = [[0]*b for _ in range(0, l)]
        visited[0][0] = 1
        while count<k and len(mins)!=0:
        	cur = heapq.heappop(mins)
        	count+=1
        	if count == k:
        		return cur[0]
        	next = get_next(cur[1][0], cur[1][1], l, b)
        	for n in next:
        		if visited[n[0]][n[1]]==0:
	        		heapq.heappush(mins, (matrix[n[0]][n[1]],n))
	        		visited[n[0]][n[1]] = 1

a = [[]]
s=Solution()
print(s.kthSmallest(a, 2))
# for k in range(1, 9):
# 	print(k, s.kthSmallest(a, k))