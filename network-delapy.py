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
                if adjMatrix[root][i] != 0 and root != i:
                    children.append([i, adjMatrix[root][i]])
            return children


        adj = [[0]*(N+1) for _ in range(0, N+1)]
        for info in timesinfo:
            adj[info[0]][info[1]] = info[2]

        print_2d_array(adj)

        times = [float("inf")]*(N+1)
        times[K] = 0
        queue = deque([K])
        visited = set()
        while len(queue) != 0:
            cur = queue.popleft()
            if cur not in visited:
                dist = times[cur]
                children = get_children(cur, adj, N+1)
                # print(cur, children)
                for c, d in children:
                    times[c] = min(times[c], dist+d)
                    queue.append(c)
                visited.add(cur)
            print(times)
        ans = 0
        for i in range(1, N+1):
            if times[i] == float("inf"):
                return -1
            elif times[i] > ans:
                ans = times[i]
        return ans


tinof=[[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
K=5
N=5
s=Solution()
print(s.networkDelayTime(tinof, N, K))