from collections import deque
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def get_children(adjmatrix, root, size):
        	children=[]
        	for i in range(0, size):
        		if adjmatrix[root][i] == 1 and root!=i:
        			children.append(i)
        	return children

        size = len(M)
        visited = [0]*size
        circles = 0
        while True:
        	cur = None
        	for i in range(0, size):
        		if visited[i] == 0:
        			cur = i 
        			visited[cur] = 1
        			break
        	if cur is None:
        		break
        	queue = []
        	queue.append(cur)
        	while len(queue) != 0:
        		cur_root = queue.pop()
        		children = get_children(M, cur_root, size)
        		for child in children:
        			if visited[child] == 0:
        				queue.append(child)
        				visited[child] = 1
        	circles += 1
        return circles


M=[]
s=Solution()
print(s.findCircleNum(M))