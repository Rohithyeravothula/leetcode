from extras import *


from collections import deque
class Solution:
    def networkDelayTime(self, timesinfo, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        def get_children(root, adjMatrix, N):
            children = []
            for i in range(0, N):
                if adjMatrix[root][i] != -1 and root != i:
                    children.append([i, adjMatrix[root][i]])
            return children


        adj = [[-1]*(N+1) for _ in range(0, N+1)]
        for info in timesinfo:
            adj[info[0]][info[1]] = info[2]

        # print_2d_array(adj)

        times = [float("inf")]*(N+1)
        times[K] = 0
        queue = deque([K])
        # visited = set()
        count = 0
        while len(queue) != 0:
            cur = queue.popleft()
            # if cur not in visited:
            dist = times[cur]
            children = get_children(cur, adj, N+1)
            # print(cur, children)
            for c, d in children:
                times[c] = min(times[c], dist+d)
                queue.append(c)
                # visited.add(cur)
            # print(times)
            count+=1
            if count > 10000:
                break
        ans = 0
        for i in range(1, N+1):
            if times[i] == float("inf"):
                return -1
            elif times[i] > ans:
                ans = times[i]
        return ans


tinof = [[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]]
N=5
K=3
s=Solution()
print(s.networkDelayTime(tinof, N, K))