class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def get_children(r):
            c=[]
            for i in range(0, numCourses):
                if i!=r and adj[r][i] == 1:
                    c.append(i)
            return c

        def dfs(node, visited):
            visited[node] = 1
            children = get_children(node)
            ans = True
            for c in children:
                if visited[c] == 1:
                    return False
                elif visited[c] == 0:
                    ans = dfs(c, visited)
                    if ans is False:
                        break
            visited[node] = 2
            return ans

        adj = [[0]*numCourses for _ in range(0, numCourses)]
        for i in prerequisites:
            adj[i[1]][i[0]] = 1

        explored = [0]*numCourses
        ans = True
        for e in range(0, numCourses):
            if explored[e] == 0:
                ans = dfs(e, explored)
                if ans is False:
                    break
        return ans

n=4
a=[[1,0], [2,1], [2,0]]
s=Solution()
ans = s.canFinish(n, a)
print(ans)

