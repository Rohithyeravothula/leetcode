class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = [[0]*numCourses for _ in range(0, numCourses)]
        for i in prerequisites:
            adj[i[1]][i[0]] = 1

        def get_children(a, r):
            children = []
            for i in range(0, numCourses):
                if a[r][i] == 1 and i!=r:
                    children.append(i)
            return children

        def dfs(node, result, visited, adj_matrix, cycle):
            visited[node] = 1
            children = get_children(adj_matrix, node)
            for c in children:
                if visited[c] == 1:
                    return False
                elif visited[c] != 2:
                    dfs(c, result, visited, adj_matrix, cycle)
            visited[node] = 2
            result.append(node)

        explored = [0]*numCourses
        cycle = False
        ans = []
        for i in range(0, numCourses):
            if explored[i] == 0:
                dfs(i, ans, explored, adj, cycle)
        ans = ans[::-1]
        if len(ans) == numCourses:
            return True
        return False

# n=8
# a=[[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]

# n=4
# a=[[2,1],[3,2],[3,1]]
n=4
a=[[1,0], [2,1], [3,2], [0, 3]]
s=Solution()
print(s.findOrder(n,a))